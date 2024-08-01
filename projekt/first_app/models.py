from django.db import models
from django.shortcuts import reverse

# Create your models here.
class user(models.Model):
    id = models.IntegerField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'[{self.id}]  {self.title}'

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'cislo':self.id})

class expense(models.Model):
    id = models.IntegerField(max_length=50)
    name = models.CharField(max_length=50)
    cost = models.FloatField()
    time = models.DateTimeField()
    owner_id = models.IntegerField(max_length=50)

    def __str__(self):
        return f'[{self.id}]  {self.title}'

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'cislo':self.id})



# Django Object-Relational Mapper (ORM) - API
# Hromada příkazů na ruční zadávání prvků do databáze atp.