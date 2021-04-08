from django.db import models
from .category import Categorie
from django.urls import reverse
#category=models.ForeignKey(Categorie, on_delete=models.CASCADE)
#category=models.CharField(max_length=100)

class Recipe(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Categorie, on_delete=models.SET_DEFAULT,default='Food')
    description=models.TextField(max_length=500)
    ingredients=models.TextField(max_length=1000)
    method=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    

    def get_ingredient_list(self):
        return self.ingredients.split('\n')

    
    def get_latest_recipes():
        latest_recipes=[]
        r=Recipe.objects.order_by('-pk')
        for i in range(4):
            latest_recipes.append(r[i])
        return latest_recipes
      

    @staticmethod
    def get_all_recipes():
        return Recipe.objects.all()

    
    
