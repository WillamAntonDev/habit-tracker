from django.urls import path
from . import views

app_name = 'habits'

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('create/', views.create_habit, name='create_habit'),
    path('<int:habit_id>/complete/', views.mark_completed, name='mark_completed'),
    path('register/', views.register, name='register'),
    path('<int:habit_id>/edit/', views.edit_habit, name='edit_habit'),
    path('<int:habit_id>/delete/', views.delete_habit, name='delete_habit'),
]