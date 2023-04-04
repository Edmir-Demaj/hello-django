from django.shortcuts import render
from .models import Item
# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
# render function takes http request and a template name as it's two arguments
# and return http response which renders that template


# def say_hello(request):
#     # when this function is called all he does is  takes an http requests
#     # from the user and return http response that says "Hello!""
#     return HttpResponse("Hello!")

# to make this function available to web browser we use urls.py
