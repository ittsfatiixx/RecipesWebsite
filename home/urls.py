from django.contrib import admin
from django.urls import path
from home import views
from .views import HomeView, RecipeMethodView, AddRecipeView,CategoryView

urlpatterns = [
    #path("", views.index, name='home'),
    path('', HomeView.as_view() ,name='home'),
    path('method/<int:pk>',RecipeMethodView.as_view(), name='how-to-make-'),
    path('add-recipe', AddRecipeView.as_view() , name='add-recipe'),
    path("<str:categ>",CategoryView, name='category'),
    
]