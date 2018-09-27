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
        # Creating a new editor and saving it
        self.yvon= Photoeditor(first_name = 'Ojijo', last_name ='Cly')
        self.yvon.save_photoeditor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()           