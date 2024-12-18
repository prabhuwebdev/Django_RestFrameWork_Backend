from django.db import models

# Create your models here.
class Color(models.Model):
    color_name=models.CharField(max_length=200)
    def __str__(self):
        return self.color_name
class Person(models.Model):
    color=models.ForeignKey(Color,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=300)
    Age=models.IntegerField()


    def __str__(self):
        return self.Name