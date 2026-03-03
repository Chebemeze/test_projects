from django.apps import AppConfig


class BookShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book_shop'

    def ready(self):
        import book_shop.signals
