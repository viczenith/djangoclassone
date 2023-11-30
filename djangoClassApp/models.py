from django.db import models

# Create your models here.
class Students(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    
class Detail(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=10000)

class Service(models.Model):
    seviceSubtitle = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=20000)
    
