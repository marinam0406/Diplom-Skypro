from django.contrib import admin

from educational_modules.models import EduModel


@admin.register(EduModel)
class EduModelAdmin(admin.ModelAdmin):
    '''
    Интерфейс администратора для модели EduModel.
    '''
    list_display = (
        "number",
        "name",
        "description",
    )
