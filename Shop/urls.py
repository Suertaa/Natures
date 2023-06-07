from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('adoption/<id>/', views.adoption, name="adoption"),
    path('category_products/<id>/', views.category_products, name="category_products"),
    path('contact/' , views.contact, name="contact"),
    path('login/', views.login, name='login'),
    path("logout/", views.logout, name= "logout"),
    path('register/', views.register, name='register'),
]