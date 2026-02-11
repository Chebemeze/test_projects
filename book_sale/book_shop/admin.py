from django.http import HttpResponse
from django.contrib import admin
from book_shop.models import Book, Product
from django.urls import path, include
from django.shortcuts import render

# Register your models here.

#  Using admin actions to perform bulk tasks to multiple objects
@admin.action(description="Mark selected book unavailable")
def mark_unavailable(modeladmin, request, queryset):
  updated = queryset.update(is_available = False)
  modeladmin.message_user(request, f"{updated} book(s) marked as unavailable")

@admin.action(description= "Mark selected book available")
def mark_available(modeladmin, request, queryset):
  updated = queryset.update(is_available = True)
  modeladmin.message_user(request, f"{updated} book(s) marked as available")

# a customized availability filter that is subclass of the
# SimpleListFilter
class AvailabilityFilter(admin.SimpleListFilter):
  title = "Availability"
  parameter_name = "availability"

  # helps django render the filter options
  def lookups(self, request, model_admin):
    return (
      ('available', 'Available'),
      ('unavailable', 'Unavailable'),
    )
  
  
  def queryset(self, request, queryset):
    if self.value() == 'available':
      return queryset.filter(is_available=True)
    
    if self.value()== 'unavailable':
      return queryset.filter(is_available=False)

class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'Author',)
  search_fields = ('title', 'Author',)

  # customized list filter
  list_filter = (AvailabilityFilter,)

  # This sets how the Book form fields are arranged on the form.
  # They are arranged in sections.
  fieldsets = (
    ('Enter Book Details', {'fields': ('title', 'Author', 'SNB', 'is_available'), 'classes':('collapse',),}),
  )

  # calling the admin action function
  actions = [mark_unavailable, mark_available,]


  # Creating admin custom view. this view will help admin to see the total books
  # and available books
  def get_urls(self):
    urls = super().get_urls()

    custom_urls = [
      path('stats/', self.admin_site.admin_view(self.stats_view), name='stats_view',),
    ]
    return custom_urls + urls

  def stats_view(self, request):
    total_books = Book.objects.count()
    # queryset = Book.objects.all()
    available_books = Book.objects.filter(is_available=True).count()

    # each_context handles context of django admin site. brings admin title
    # header, url, ect into this view created
    context = {
      'available_books': available_books,
      'total_books': total_books,
      **self.admin_site.each_context(request),
    }
    return render(request, 'book_shop/base.html',context)


class ProductAdmin(admin.ModelAdmin):
  fieldsets = (
    ('Basic Information', {'fields':('name', 'description'),}),
    ('Pricing', {'fields':('price', 'Discount_price'),}),
    ('Inventory', {'fields': ('stock', 'is_active'),}),
    ('Internal note', {'fields': ('internal_note',),'classes': ('collapse',),}),
    ('system info', {'fields': ('created_at',),}),
  )

  # readonly_fields is used to display the non editable field- create_at field in the form
  readonly_fields = ('created_at',)


# Fields are used to arrange the fields that would be displayed in the Book form
#   fields = (
#     'name',
#     'description',
#     'price',
#     'Discount_price',
#     'stock',
#     'is_active',
#   )

# registers the Book model and Bookadmin that customizes it
admin.site.register(Book, BookAdmin)

# registers the Product model and ProductAdmin that customises it
admin.site.register(Product, ProductAdmin)
