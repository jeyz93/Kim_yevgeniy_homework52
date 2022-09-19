from django.contrib import admin
from webapp.models import Tasks


class TasksAdmin(admin.ModelAdmin):
    list_display = ('description', 'set_st', 'data_do')
    list_editable = ['set_st']
    list_filter = ('id', 'description')


admin.site.register(Tasks, TasksAdmin)
