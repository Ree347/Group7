from django.db import models

# Create your models here. Model for the database create
# Always make the classes singular


class Member(models.Model):
    fname = models.CharField(max_length = 100)
    lname = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    passwd = models.CharField(max_length = 50)
    age = models.IntegerField()
    
    def __str__(self):
        return self.fname + ' ' + self.lname