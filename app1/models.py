from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
# Contact is Table
class Contact(models.Model):

 # Columns names in Contact Table
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=10)
    desc = HTMLField()
    date = models.DateField()

# This shows the name of user in database
    def __str__(self):
        return f'{self.name}'
    
class ICDetail(models.Model):
    name = models.CharField(max_length=120)
    img = models.ImageField(upload_to='home_imgs')
    quantity = models.IntegerField()
    price = models.IntegerField()
    Desc = HTMLField()
    icecream_slug = AutoSlugField(populate_from = 'name', unique=True, null=True, default= None)
    

    
