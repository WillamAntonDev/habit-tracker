from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, HabitLog
from datetime import date
from django.contrib.auth.decorators import login_required

@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)
    today = date.today()
    logs = HabitLog.objects.filter(habit__in=habits, date=today)

    return render(request, 'habits/habit_list.html', {
        'habits': habits,
        'logs': {log.habit.id: log for log in logs}
    })

@login_required
def mark_completed(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    today = date.today()
    log, created = HabitLog.objects.get_or_create(habit=habit, date=today)
    log.completed = not log.completed
    log.save()
    return redirect('habits:habit_list')
