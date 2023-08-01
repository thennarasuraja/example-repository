from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def form(request):
    return render(request,"jerry.html")

def output(request):
    name=request.POST["Name"]
    password=request.POST["Password"]
    address=request.POST["Address"]
    mail=request.POST["Mail"]
    return render(request,"result.html",{"Name":name,"Password":password,"Address":address,"Mail":mail})