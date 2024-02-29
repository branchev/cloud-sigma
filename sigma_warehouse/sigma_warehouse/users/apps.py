from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sigma_warehouse.users'

    def ready(self) -> None:
        import sigma_warehouse.users.signals
        return super().ready()