from turtle import title
from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length= 50, verbose_name= "Başlık")
    completed = models.BooleanField(verbose_name= "Durum")
    
    def __str__(self) -> str:
        return f"{self.title}: {self.completed}"