from django.shortcuts import render
from django.template import loader
from .models import Workout
from django.http import HttpResponse


def workouts(request):
    latest_workouts_list = Workout.objects.order_by('name')
    template = loader.get_template('pages/workouts.html')
    context = {
        'latest_workouts_list': latest_workouts_list,
    }
    return render(request, 'pages/workouts.html', context)


def start(request):
    latest_workouts_list = Workout.objects.order_by('name')
    template = loader.get_template('pages/start_workout.html')
    context = {
        'latest_workouts_list': latest_workouts_list,
    }
    return render(request, 'pages/start_workout.html', context)


def startWorkout(request, workout_id):
    active_workout = Workout.objects.get(pk=workout_id)
    return render(request, "pages/working_out.html", {'workout': active_workout})
