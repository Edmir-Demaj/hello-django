from django import forms
from .models import Item
# create forms from django in order to avoid validation errors
# first import forms and Item model


class ItemForm(forms.ModelForm):
    # our form is a class that inherits built in django class
    # to give basic funcionality by inheriting ModelForm
    class Meta:
        # this inner class provides meta about form itself
        model = Item
        fields = ['name', 'done']
