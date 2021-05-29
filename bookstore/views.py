from django.shortcuts import render
from django.http import HttpResponse

def firstviewfunction(request):
    response = HttpResponse("<h1>Here's the text of the web page.</h1>")
    response.status_code = 404
    response['Age'] = 120
    return response