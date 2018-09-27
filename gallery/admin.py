from django.contrib import admin
from .models import Photoeditor,Category,Image

# Register your models here.
admin.site.register(Photoeditor)
admin.site.register(Category)
admin.site.register(Image)