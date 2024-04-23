from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    email=serializers.EmailField(max_length=100)
    phone=serializers.CharField(max_length=10)
    dsg=serializers.CharField(max_length=50)
    salary=serializers.IntegerField()

    def create(self,validateddata):
        return Employee.objects.create(**validateddata)
    
    def update(self,instance,validateddata):

        if ("name" in validateddata and validateddata['name']!=""):
            instance.name=validateddata["name"]

        if ("email" in validateddata and validateddata['email']!=""):
            instance.email=validateddata["email"]

        if ("phone" in validateddata and validateddata['phone']!=""):
            instance.phone=validateddata["phone"]

        if ("dsg" in validateddata and validateddata['dsg']!=""):
            instance.dsg=validateddata["dsg"]

        if ("salary" in validateddata and validateddata['salary']!=""):
            instance.salary=validateddata["salary"]

        instance.save()
        return instance