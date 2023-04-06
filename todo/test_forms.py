from django.test import TestCase
# class TEstCase is an extension of the python standart
# library module called unit tests
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):
    # inside our class every test will be defined as a method

    def test_item_name_is_required(self):
        # first inisiate a form without a name that simulates a
        # form submitted without name
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        # check if name key is in the dictionary of form errors
        self.assertIn('name', form.errors.keys())
        # check if error message on name field is == This field is required
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_is_not_required(self):
        # to test if done status is not required we create the form and
        # send it without done status
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        # this tests if form is submited with only name and done field
        form = ItemForm()  # first create an empty form
        self.assertEqual(form.Meta.fields, ['name', 'done'])
