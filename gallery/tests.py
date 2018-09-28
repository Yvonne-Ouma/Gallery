from django.test import TestCase
import datetime as dt

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

    # def test_save_method(self):
    #     self.yvon.save_photoeditor()
    #     yvon = Photoeditor.objects.all()
    #     self.assertTrue(len(yvon) > 0)  

        
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

    def test_get_posts_today(self):
        today_posts = Image.todays_posts()
        self.assertTrue(len(today_posts)>0)


    

#........
    def test_get_posts_by_date(self):
            test_date = '2017-03-17'
            date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
            posts_by_date = Article.days_posts(date)
            self.assertTrue(len(posts_by_date) == 0)              
