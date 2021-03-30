from django.shortcuts import render
from django.http import HttpResponse

def index (request):
	myname = "曾稜雅"
	return render(request, 'index.html', locals())
