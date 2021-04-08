from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView


from datetime import datetime
#from home.models import Contact
from django.contrib import messages
from .models.recipe import Recipe
from .models.category import Categorie

c= Categorie.get_all_categories()
# Create your views here.
'''
def index(request):
    r= Recipe.get_all_recipes()
    return render(request, 'index.html',{'recipes':r,'categories':c})
    # return HttpResponse("this is homepage")
'''

class HomeView(ListView):
    model= Recipe
    context_object_name='recipes'
    template_name= 'index.html'
    def get_context_data(self, **kwargs):
        category_menu=Categorie.objects.all()
        latest_recipes=Recipe.get_latest_recipes()
        context=super(HomeView,self).get_context_data(**kwargs)
        context['category_menu']=category_menu
        context['latest_recipes']=latest_recipes
        return context


class RecipeMethodView(DetailView):
    model= Recipe
    template_name= 'recipeMethod.html'
    def get_context_data(self, **kwargs):
        category_menu=Categorie.objects.all()
        context=super(RecipeMethodView,self).get_context_data(**kwargs)
        context['category_menu']=category_menu
        return context

class AddRecipeView(CreateView):
    model= Recipe
    template_name= 'addRecipe.html'
    fields= '__all__'

def CategoryView(request,categ):
    category_menu=Categorie.objects.all()
    category_recipes=Recipe.objects.filter(category=categ.replace('-',' '))
    return render(request,'category.html',{'categ':categ.replace('-',' ') ,'category_menu':category_menu, 'recipe_list':category_recipes })

'''
def category(request):
    clist=Categorie.get_categories()
    return render(request, 'category.html',{'list':clist,'categories':c}) 


def dessert(request):
    return render(request, 'category.html', {})


def services(request):
    return render(request, 'services.html')
'''

'''
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
 '''