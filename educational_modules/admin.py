from django.contrib import admin

from educational_modules.models import EduModel


@admin.register(EduModel)
class EduModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
