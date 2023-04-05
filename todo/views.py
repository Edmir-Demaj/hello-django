from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
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

def add_item(request):
    if request.method == 'POST':
        # check which method is requested get/post
        # if is post then get the value of name and
        # the boolean value of done
        form = ItemForm(request.POST)  # create form instance
        if form.is_valid():  # validate form
            form.save()  # save form
        # name = request.POST.get('item_name')
        # done = 'done' in request.POST
        # checks if post data has done property in it
        # Item.objects.create(name=name, done=done)
            return redirect('get_todo_list')
    form = ItemForm()  # this is an instance of class ItemForm
    context = {
        'form': form  # context contain form itself
    }

    return render(request, 'todo/add_item.html', context)
    # return the context to template to render
