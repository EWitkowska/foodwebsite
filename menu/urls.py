from . import views
from django.urls import path
from menu import views as menu_views

app_name = 'menu'
urlpatterns = [
    path('menu/',menu_views.menu,name='menu'),
]