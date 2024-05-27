from django.db import models

# Create your models here.

'''
Note by Emzy: All the user defined models(tables) must inherit the base class Model from 
django.db.models
To make DB migrations - run python manage.py makemigrations
Migration generates corresponding sql commands for all changes done in models.py module
'''

class Skills(models.Model):
    emailid = models.CharField(max_length=250)
    skills = models.TextField()