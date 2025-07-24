from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"