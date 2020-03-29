from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Wow")

def insertData(request):
    return render(request, "index.html")