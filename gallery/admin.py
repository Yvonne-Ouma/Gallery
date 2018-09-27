from django.contrib import admin
from .models import Photoeditor,Category,Image

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('Category',)

# Register your models here.
admin.site.register(Photoeditor)
admin.site.register(Category)
admin.site.register(Image, ImageAdmin)