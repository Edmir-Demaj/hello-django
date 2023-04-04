from django.db import models

# Create your models here.
# To have funcionality in one class from another class all we need to do
# is to inherit the one we need


class Item(models.Model):
    # when define a class, class name should be always capital Letter
    # this class is like a sheet in our database created from django
    # in order for our class to have funcionality we need to iherit
    # the base model class inside our class.
    name = models.CharField(max_length=50, null=False, blank=False)
    # only characters or text allowed inside
    # prevent creation of todo items without name
    # prevent items without a name programatically
    # blank makes field required on forms
    done = models.BooleanField(null=False, blank=False, default=False)
    # only boolean values allowed, default false mean items are not done

    def __str__(self):
        # override string on django.db and takes self which is class itself and
        # return item classe name attribute which is the name we put into form
        return self.name
