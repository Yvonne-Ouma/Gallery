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

        
class ImageTestClass(TestCase):
    
    def setUp(self):
        # Creating a new photoeditor and saving it
        self.yvon= Photoeditor(first_name = 'Ojijo', last_name ='Cly')
        self.yvon.save_photoeditor()

        # Creating a new category and saving it
        self.new_category = Category(name = 'fassion')
        self.new_category.save()

        self.new_image= Image(title = 'show case', name = 'trouser',description = 'it looks good',photoeditor = self.yvon)
        self.new_image.save()

        self.new_image.category.add(self.new_category)

    def tearDown(self):
        Photoeditor.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()           
