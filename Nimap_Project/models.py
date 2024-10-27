from datetime import timezone
from django.db import models
from datetime import datetime

# Create your models here.

class client(models.Model):
    client_name = models.CharField(max_length=100)
    created_at= models.DateTimeField(auto_now_add=True)
    created_by= models.CharField(max_length=50)

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(client, related_name='projects', on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    created_by= models.CharField(max_length=50)

class User(models.Model):
    user_name = models.CharField(max_length=255)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=14)
    # client = models.ForeignKey(client, related_name='users', on_delete=models.CASCADE)
    # project= models.ForeignKey(Project, related_name='users', on_delete=models.CASCADE)
    