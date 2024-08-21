from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''
    Admin interface for the User model. Displays the id and email of each user.
    '''
    list_display = (
        "id",
        "email",
    )
