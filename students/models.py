from django.db import models

# Create your models here.
#Table student
class Students(models.Model):
    student_number=models.PositiveIntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    Grade = models.CharField(max_length=2)

    def __str__(self) -> str:
        return f'students {self.first_name}'