from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    has_job = models.BooleanField(default=False)
    is_happy = models.BooleanField(default=False)

    def take_a_job(self):
        self.has_job = True

    def smile(self):
        self.is_happy = True
