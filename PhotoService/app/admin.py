from django.contrib import admin
from .models import Category, Photo

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_displey_links = ('id', 'title')

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_displey_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
