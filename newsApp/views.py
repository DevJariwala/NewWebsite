from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json
import requests

# Create your views here.
def index(request):
     news_api_request = requests.get('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=5bfe7f83d50e49f08f8141cb6e4f956e')
    # fetch the api
     api = json.loads(news_api_request.content)
     return render(request,"newsApp/index.html",{'api':api})
      

