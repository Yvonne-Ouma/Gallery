from django.test import TestCase
import datetime as dt

# Create your tests here.
from django.test import TestCase
from .models import Location,Category,Image

class LocationTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.yvon = Location(name = "Nairobi")

    # Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.yvon,Location)) 

