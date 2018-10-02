from django.test import TestCase
import datetime as dt
from .models import Location,Category,Image

# Create your tests here.



class GalleryTestCAses(TestCase):
    def setUp(self):
        self.new_category = Category(name = 'Technology')
        self.new_category.save_category()
        self.new_location = Location(name = 'Nairobi')
        self.new_location.save_location()
        self.new_image = Image(id = 1, title = 'Gaming', name = 'Game', description = 'this the best game', image = 'media/gallery/drink.jpg', location = self.new_location)
        

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_category,Category))
        self.assertTrue(isinstance(self.new_location,Location))


    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)
        
    def test_delete_method(self):
        self.new_image.delete_image()
        all_objects = Image.objects.all()
        self.assertFalse(len(all_objects)>0)  
    

