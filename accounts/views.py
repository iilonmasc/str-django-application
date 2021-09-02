from django.shortcuts import render
from django.http import HttpResponse

def list(request):
    return HttpResponse("accounts.list view")

# Create your views here.
