from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('schedule/', views.schedule, name='schedule'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('login/', views.signin, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]