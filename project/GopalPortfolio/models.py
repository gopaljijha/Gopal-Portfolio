from django.db import models
from django.contrib.auth.models import User
from django.forms import ComboField
from django import forms
import re

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=40)
    


    def __str__(self):
        return self.name