from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name ='home'),
    path('about', views.about, name ='about'),
    path('index', views.index, name ='index'),
    path('add'  , views.add  , name = 'add'),
    path('add/addrecord', views.addrecord, name='addrecord'),
    path('subscription',views.subscription,name='subscription'),
    path('subscription/thankyou',views.thankyou_subscription,name='thankyou_subscription'),
    path('<str:id>',views.id,name='id'), #dynamic link
]