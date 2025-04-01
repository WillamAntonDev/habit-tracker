from django.contrib import admin
from.models import Habit

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'created_at')

@admin.register(HabitLog)
class HabitLogAdmin(admin.ModelAdmin):
    list_display = ('habit', 'date', 'completed')
    search_fields = ('habit__name',)
    list_filter = ('completed', 'date')    
