from django.db import models

class Categorie(models.Model):
    category=models.CharField(max_length=200,primary_key=True)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('home')
    
    @staticmethod
    def get_all_categories():
        return Categorie.objects.all()

    @staticmethod
    def get_categories():
        c= Categorie.objects.all()
        clist=[]
        for i in range(2):
            clist.append(c[i])
        return clist
