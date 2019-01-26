from django.db import models
from users.models import CustomUser 
import uuid #for unique book instances 
from datetime import date

class Books(models.Model):    
    name = models.CharField(max_length = 200)
    author = models.CharField (max_length = 200)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True)
    is_assigned = models.BooleanField(default=False)

    def __str__(self):
        return self.name
