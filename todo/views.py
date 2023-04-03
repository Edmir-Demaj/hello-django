from django.shortcuts import render, HttpResponse

# Create your views here.


def say_hello(request):
    # when this function is called all he does is  takes an http requests
    # from the user and return http response that says "Hello!""
    return HttpResponse("Hello!")

# to make this function available to web browser we use urls.py
