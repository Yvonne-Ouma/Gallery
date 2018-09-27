from django.contrib import admin
from .models import Photoeditor,Image,Category

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)

# Register your models here.
admin.site.register(Photoeditor)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category)
