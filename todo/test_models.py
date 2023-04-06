from django.test import TestCase
# class TEstCase is an extension of the python standart
# library module called unit tests
from .models import Item

# Create your tests here.
# here we will test that our todo items will be created by default
#  with the done status of false


class TestModels(TestCase):
    # inside our class every test will be defined as a method

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertEqual(str(item), 'Test Todo Item')
