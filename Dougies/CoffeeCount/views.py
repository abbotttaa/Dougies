from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse ("<h2>Oh shit waddup, it's CoffeeCount.</h2>")

# Create your views here.
