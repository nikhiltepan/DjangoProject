from django.db import models

# Create your models here.
class Dreamreal (models.Model):
    website=models.CharField(max_length=50)
    mail = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    phonenumber = models.IntegerField()
    online = models.ForeignKey('online', on_delete=models.PROTECT, default =1 ) #on_delete=models.,
    
    class Meta: 
        db_table="dreamreal"

class Online(models.Model):
    domain= models.CharField(max_length=50)

    class meta :
        db_table = "online"
