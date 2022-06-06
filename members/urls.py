from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name ='home'),
    path('about', views.about, name ='about'),
    path('index', views.index, name ='index'),
    path('add'  , views.add  , name = 'add'),
    path('add/addrecord', views.addrecord, name='addrecord'),
    path('<str:id>',views.id,name='id') #dynamic link
]