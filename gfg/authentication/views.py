from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from . models import Emp
from django.http import HttpResponseRedirect
# Create your views here.

# def user(request):
#     return HttpResponse("Hello World")

def user(request):
    if request.method == 'POST':
        empname = request.POST['name']
        empemail = request.POST['email']
        emppass= request.POST['password']
        data = Emp(Emp_name=empname,Emp_email=empemail,Emp_password=emppass)
        data.save()
        return render(request,'index.html')
    return render(request,'index.html')


def details(request):
    if request.method == "GET":
        a = Emp.objects.all()
        return render(request,"data.html",{'data':a})
    elif request.method == "POST":
        return HttpResponseRedirect(request.path)    

def Update_record(request):
    if request.method == "POST":
        id = request.POST['id']  
        name = request.POST['name']   
        email = request.POST['email']   
        password = request.POST['password'] 

        b = get_object_or_404(Emp,pk=id)
        b.Emp_name = name
        b.Emp_email = email
        b.Emp_password = password
        b.save()
        return HttpResponseRedirect('/data/')

def Delete_record(request,id):
    if request.method == "POST":
        a = Emp.objects.get(pk=id)
        a.delete()
        return redirect('/data/')


