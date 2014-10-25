from django.db import models

# Create your models here.

class Item(models.Model):
    item_text = models.CharField(max_length=200)

#class User(models.User):
#    id = models.AutoField(primary_key=True)

