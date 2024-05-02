from django.db import models

# Create your models here.

class students(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    grade = models.IntegerField()
    faculty = models.CharField(max_length=10)
    description = models.TextField(max_length = 150)
    nationality = models.BooleanField(default = False)
    stuimg = models.ImageField(upload_to='images/',null =True, default="")
    is_selected = models.BooleanField(default = False)
    