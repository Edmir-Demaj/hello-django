from django.test import TestCase
# class TEstCase is an extension of the python standart
# library module called unit tests
from .models import Item

# Create your tests here.


class TestViews(TestCase):
    # inside our class every test will be defined as a method

    def test_get_todo_list(self):
        # test home page
        response = self.client.get('/')  # check if bring to home page
        self.assertEqual(response.status_code, 200)  # check return status code
        self.assertTemplateUsed(response, 'todo/todo_list.html')
        # confirm if we are using the correct template to render

    def test_get_add_item_page(self):
        # test getting the add page
        response = self.client.get('/add')  # check if bring to add page
        self.assertEqual(response.status_code, 200)  # check return status code
        self.assertTemplateUsed(response, 'todo/add_item.html')
        # confirm if we are using the correct template to render

    def test_get_edit_item_page(self):
        # test getting the edit page
        item = Item.objects.create(name='Test Todo Item')  # create an item
        response = self.client.get(f'/edit/{item.id}')  # use f-string
        # check if bring to edit page with same ID
        self.assertEqual(response.status_code, 200)  # check return status code
        self.assertTemplateUsed(response, 'todo/edit_item.html')
        # confirm if we are using the correct template

    def test_can_add_item(self):
        # test can add item
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        # test can delete item
        item = Item.objects.create(name='Test Todo Item')  # create an item
        response = self.client.get(f'/delete/{item.id}')  # can delete item
        self.assertRedirects(response, '/')  # check if redirect us to home pg
        existing_items = Item.objects.filter(id=item.id)
        # prove item is deleted from database
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        # test can toggle item
        item = Item.objects.create(name='Test Todo Item', done=True)
        # create an item with a done status of true
        response = self.client.get(f'/toggle/{item.id}')  # can toggle item
        self.assertRedirects(response, '/')  # check if redirect us to home pg
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
        # checks if our done status True is changed to False after toggle
