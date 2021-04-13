from django.db import models
from django import forms
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_plan = models.CharField(max_length=128,default=None,blank = False)

class Ticket(models.Model):

    TICKET_STATUS = (
        ('open','Open'),
        ('complete', 'Complete'),
        ('pending','Pending'),
    )

    ticketId  = models.AutoField(primary_key=True)
    title  = models.CharField(max_length=128, default=None ,blank = False)
    description = models.TextField(blank = False, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=TICKET_STATUS, default="open")
    tags = TaggableManager()

    def __str__(self):
        return self.title
