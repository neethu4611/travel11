from django.db import models
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    des = models.TextField()
    def __str__(self):
         return self.name

class team(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic')
    des=models.TextField()
    def __str__(self):
         return self.name