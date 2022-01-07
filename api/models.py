from django.db import models

# Create your models here.

class User(models.Model):
	login      = models.CharField(max_length=100)
	birth_date = models.DateField(blank=False, null=False)
	password   = models.CharField(blank=True, max_length=20)
  


def __str__(self):
	return self.login

