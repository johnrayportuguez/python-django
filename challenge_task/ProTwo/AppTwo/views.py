from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<em>My Second Project</em>")

def help(request):
    helpdict = {'insert_me': "HELP PAGE"}
    return render(request,'AppTwo/help.html',context=helpdict)