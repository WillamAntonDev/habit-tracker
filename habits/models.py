from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
      
      
class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='logs')
    date = models.DateField(default=date.today)
    completed = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('habit', 'date')
    
    def __str__(self):
        return f"{self.habit.name} - {self.date} - {'Completed' if self.completed else 'Not Completed'}"