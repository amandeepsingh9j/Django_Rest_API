from django.db import models

# Create your models here.


class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=10)
    dsg=models.CharField(max_length=50)
    salary=models.IntegerField()

    def __str__(self):
        return str(self.id)+"-"+self.name
    