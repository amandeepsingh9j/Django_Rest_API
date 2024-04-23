from django.shortcuts import render,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import EmployeeSerializer
from .models import Employee
import io
from django.db.models import Q
# Create your views here.



@csrf_exempt
def createdata(Request):
    jsondata=Request.body
    stream=io.BytesIO(jsondata)
    pythondata=JSONParser().parse(stream)
    empserializer=EmployeeSerializer(data=pythondata)
    if empserializer.is_valid():
        empserializer.save()
        msg={"Result":"Successfully Created Record"}
    else:
        msg={"Result":"Failed"}
    
    jsondata=JSONRenderer().render(msg)
    return HttpResponse(jsondata,content_type="application/json")



@csrf_exempt
def getdata(Request):
    data=Employee.objects.all()
    dataserializer=EmployeeSerializer(data,many=True)
    jsondata=JSONRenderer().render(dataserializer.data)
 

    return HttpResponse(jsondata,content_type="application/json")




@csrf_exempt
def getsingledata(Request,email):
    try:    
        data=Employee.objects.get(email=email)
        empserializer=EmployeeSerializer(data,many=False)
        jsondata=JSONRenderer().render(empserializer.data)
        return HttpResponse(jsondata,content_type="application/json")

    except:
        msg={"result":"Failed"}
        jsondata=JSONRenderer().render(msg)
        return HttpResponse(jsondata,content_type="application/json")

    
    


@csrf_exempt
def deletedata(Request,email):
    data=Employee.objects.get(email=email)
    data.delete()
    msg={"result":"Successfully Deleted"}
    jsondata=JSONRenderer().render(msg)
    return HttpResponse(jsondata,content_type="application/json")


@csrf_exempt
def updatedata(Request):
    jsondata=Request.body
    stream=io.BytesIO(jsondata)
    pythondata=JSONParser().parse(stream)
    try:
        emp=Employee.objects.get(email=pythondata['email'])
        empserializer=EmployeeSerializer(emp,data=pythondata,partial=True)
        if (empserializer.is_valid()):
            empserializer.save()
        msg={"result":"Successfully updated"}
        
    except:
        msg={"result":"Failed, Something went wrong"}
    jsondata=JSONRenderer().render(msg)
    return HttpResponse(jsondata,content_type="application/json")


@csrf_exempt
def searchdata(Request):
        jsondata=Request.body
        stream=io.BytesIO(jsondata)
        pythondata=JSONParser().parse(stream)
        search=pythondata['search']
        data=Employee.objects.filter(Q(name__icontains=search)|Q(email__icontains=search)|Q(phone__icontains=search)|Q(dsg__icontains=search)|Q(salary__icontains=search))
        empserializer=EmployeeSerializer(data,many=True)
        jsondata=JSONRenderer().render(empserializer.data)
        return HttpResponse(jsondata,content_type="application/json")
    

    
