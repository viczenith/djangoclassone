from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('signout', views.signout, name='signout'),
    path('blog', views.blog, name='blog'),
    path('services', views.services, name='services'),
    path('portfolioDetails', views.portfolioDetails, name='portfolioDetails'),
    path('portfolioDetailsportfolioDetails', views.portfolioDetails, name='portfolioDetails'),
    # path('blogDetails', views.blogDetails, name='blogDetails'),
]
