from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule/', views.schedule, name='schedule'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]