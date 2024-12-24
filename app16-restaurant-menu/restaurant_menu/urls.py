from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='index'),
    path('item/<int:pk>/', views.MenuDetail.as_view(), name='menu_detail'),
]