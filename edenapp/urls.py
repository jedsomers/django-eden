from django.urls import path
from . import views

urlpatterns = [
    path('', views.design_list, name='design_list'),
]