from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.translation import gettext_lazy as _

class Task(models.Model):
    class TaskStatus(models.TextChoices):
        in_progress= 'En curso', _('En curso')
        done= 'Completado', _('Completado')
        abandoned= 'Abandonado', _('Abandonado')

    user = models.ForeignKey(User, on_delete= models.CASCADE, null= True, blank= True)
    title = models.CharField(max_length=200)
    description = models.TextField(null= True, blank= True)
    complete = models.BooleanField(default= False)
    create = models.DateTimeField(auto_now_add= True)
    status =models.CharField(max_length=50,choices=TaskStatus.choices,default=TaskStatus.in_progress)
    def __str__(self):  #define el atributo principal
        return self.title


    class Meta:
        ordering = ['complete'];




