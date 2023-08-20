from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='home'),
    path('main/', views.main, name='main'),
    path('signup', views.register, name='signup'),
    path('login', views.login_view, name='login'),
]
