from django.db import models
from django import forms

class Ticket(models.Model):    
    ticketId  = models.AutoField(primary_key=True)
    title  = models.CharField(max_length=128, default=None ,blank = False)
    description = models.TextField(blank = False, default=None)
    #userId  = models.ForeignKey(Author, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.title
