from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')


def system_home(request):
	return render(request, 'system/index.html')


def contact(request):
	return render(request, 'contact.html')



def list(request):
	return render(request, 'list.html')
