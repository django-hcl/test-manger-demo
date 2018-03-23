from django.urls import path
from .import views

urlpatterns = [
    path('test2', views.test2, name='test2'),
    path('test3', views.test3, name='test3'),

]

