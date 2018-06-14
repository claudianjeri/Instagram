from django.db import models

# Create your models here.
class Images(models.Model): # inherits from the modules.Model clss
    image = models.ImageField(upload_to = 'uploads/')
    caption = models.TextField()
    comments = models.TextField()
    profile = 
    likes =
    upload_date=


class Profile(models.Model):


class User(models.Model):


class Comments(models.Model):

class Likes(models.Model):



