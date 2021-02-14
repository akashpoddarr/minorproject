from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    query = request.GET.get('q')


if query: 
    url = 'http://www.omdbapi.com/?i=tt3896198&apikey=cfdb5a43'