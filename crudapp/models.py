from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='Student Name')
    email = models.EmailField(verbose_name='Email Address')
    address = models.CharField(max_length=200, verbose_name='Address')

    def __str__(self):
        return f"{self.name} - {self.email} - {self.address}"

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
