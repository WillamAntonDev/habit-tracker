from django.contrib import admin
from.models import Habit

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'created_at')
    
