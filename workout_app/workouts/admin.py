from django.contrib import admin
from .models import Workout, Exercise
# Register your models here.


class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 25


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'sets', 'reps']
    search_fields = ['name']
    list_per_page = 25


admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Exercise, ExerciseAdmin)
