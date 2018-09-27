from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Photoeditor,Category,Image

class PhotoeditorTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.yvon = Photoeditor(first_name = 'Yvonne', last_name = 'Ouma')

    # Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.yvon,Photoeditor)) 

    def test_save_method(self):
        self.yvon.save_photoeditor()
        yvon = Photoeditor.objects.all()
        self.assertTrue(len(yvon) > 0)     