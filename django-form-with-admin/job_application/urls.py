from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('apply/', views.apply, name='apply'),
    # path('success/', views.success, name='success'),
]