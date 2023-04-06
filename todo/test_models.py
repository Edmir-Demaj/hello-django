from django.test import TestCase
# class TEstCase is an extension of the python standart
# library module called unit tests

# Create your tests here.


class TestDjango(TestCase):
    # inside our class every test will be defined as a method

    def test_this_works(self):
        # this built-in method determine if 1==0
        self.assertEqual(1, 1)

