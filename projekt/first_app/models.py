from django.db import models

# Create your models here.
class User(models.Model):
    title = models.CharField(max_length=100)
    # Udělej mi sloupeček se jménem Article s délkou 100 znaků, bez dalších parametrů
    content = models.CharField(max_length=2000)
    # udělej mi sloupeček s obsahem, ma 2000 znaků

    def __str__(self):
        return f'[{self.id}]  {self.title}'

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'cislo':self.id})

# Django Object-Relational Mapper (ORM) - API
# Hromada příkazů na ruční zadávání prvků do databáze atp.