from django.db import models
# import datetime as dt

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length = 30)        
    

class Image(models.Model):
    title = models.CharField(max_length = 60)
    name = models.CharField(max_length = 60)
    description = models.CharField(max_length = 90)
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')


    def __str__(self):
        return self.title

    def save_Image(self):
        self.save()

    def delete_Image(self):
        self.delete()    

    @classmethod
    def todays_posts(cls):
        today = dt.date.today()
        posts = cls.objects.filter(pub_date__date = today) 
        return posts  

    @classmethod
    def days_posts(cls,date):
        posts = cls.objects.filter(pub_date__date = date)
        return posts  

    @classmethod
    def search_by_category(cls,search_term):
        gallery = cls.objects.filter(category__name__icontains = search_term) 
        return gallery  




