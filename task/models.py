from django.db import models
from category.models import Category
# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    TaskAssign_Date = models.DateField(auto_now_add=True )
    Categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.taskTitle

