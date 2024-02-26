from django.contrib import admin

from sigma_warehouse.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_superuser', )
    list_per_page = 25


admin.site.register(User, UserAdmin)
