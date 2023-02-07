from django.contrib.postgres.fields import ArrayField
from django.db import models


class Category (models.Model):
    name = models.CharField (max_length=500)

    def __str__(self):
        return self.name

class Question (models.Model):
    title = models.CharField(max_length=500)
    options = ArrayField(models.CharField(max_length=200), null=True, blank=True)
    correct_option = models.CharField(max_length=100)
    category =  models.ForeignKey(Category, null=True, blank=True, on_delete= models.CASCADE)

    def __str__(self):
        return self.title
 
