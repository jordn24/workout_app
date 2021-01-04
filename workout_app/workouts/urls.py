from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.workouts, name='workouts'),
    path('start', views.start, name='start'),
    path('start/<int:workout_id>', views.startWorkout, name='startWorkout'),
]
