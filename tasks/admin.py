from django.contrib import admin
from .models import task

# Register your models here.

@admin.register(task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','completed','created_at','user')
    list_filter = ('completed','created_at')
    search_fields = ('title','description')