from operator import mod
from venv import create
from django.db import models


class Track(models.Model):
    track_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.track_name


# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, default="no name")
    age = models.IntegerField()
    student_track = models.ForeignKey(Track, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.fname + " " + self.lname

    def is_adult(self):
        if self.age > 15:
            return True
        else:
            return False

    is_adult.short_description = "Adult or not"
    is_adult.boolean = True
