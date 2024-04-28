from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from matplotlib import pyplot as plt
import os

# Create your models here.

class Zdarzenie(models.Model):
    id = models.IntegerField(primary_key=True)
    ti = models.IntegerField(default=0)
    tj = models.IntegerField(default=0)
    float_value = models.IntegerField(default=0)


class Czynnosc(models.Model):
    name = models.CharField(max_length=20)
    duration = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)])
    before = models.IntegerField(validators=[MinValueValidator(1)])
    after = models.IntegerField(validators=[MinValueValidator(1)])


class CPM(models.Model):
    file_name = models.CharField(max_length=20)
    activityAmount = models.IntegerField()  #czynnosci
    eventAmount = models.IntegerField()     #zdarzenia

