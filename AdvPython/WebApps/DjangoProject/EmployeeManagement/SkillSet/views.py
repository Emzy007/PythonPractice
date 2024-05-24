from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse('<h1> Welcome to Employee Management System</h1>')

def updateskillset(request):
    return render(request, 'updateskillset.html')