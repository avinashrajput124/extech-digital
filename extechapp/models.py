from django.db import models


class student_register(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    fathername=models.CharField(max_length=245)
    starts_on=models.CharField(max_length=100)
    ends_on=models.CharField(max_length=100)
    def __str__(self):
        return self.first_name

