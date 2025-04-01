from django.urls import path
from . import views

app_name = 'habits'

urlpatterns = [
  path('', views.habit_list, name='habit_list'),
  path('<int:habit_id>', views.mark_completed, name='mark_completed'),
  
]