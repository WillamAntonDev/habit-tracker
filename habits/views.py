from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import HabitForm
from django.contrib.auth import login
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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registering
            return redirect('habits:habit_list')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

@login_required
def create_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habits:habit_list')
    else:
        form = HabitForm()
    
    return render(request, 'habits/create_habit.html', {'form': form})
