from django.urls import path

from portfolio import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bkp', views.bkp, name='bkp'),
]