from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    reps = models.IntegerField()
    sets = models.IntegerField()

    def __str__(self):
        return self.name + " " + str(self.sets) + "x" + str(self.reps)


class Workout(models.Model):
    name = models.CharField(max_length=100)
    exercise = models.ManyToManyField(Exercise)
    models.ForeignKey(Exercise, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
