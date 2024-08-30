from django.contrib import admin

from educational_modules.models import EduModel


@admin.register(EduModel)
class EduModelAdmin(admin.ModelAdmin):
    '''
    Admin interface for EduModel model.
    '''
    list_display = (
        "id",
        "name",
        "description",
    )
