from django.contrib import admin
#from home.models import Contact
from .models.recipe import Recipe
from .models.category import Categorie

class AdminRecipe(admin.ModelAdmin):
    list_display=['name','category']

class AdminCategory(admin.ModelAdmin):
    list_display=['category']

# Register your models here.
#admin.site.register(Contact)
admin.site.register(Recipe, AdminRecipe)
admin.site.register(Categorie,AdminCategory)