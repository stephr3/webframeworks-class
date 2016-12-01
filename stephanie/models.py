from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    project = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ('name',)
