from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('apply/', views.apply, name='apply'),
    # path('success/', views.success, name='success'),
]