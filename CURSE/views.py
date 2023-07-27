
from django.http import HttpResponse
from django.shortcuts import render

def aboutView(request):
    return render(request, "about.html")