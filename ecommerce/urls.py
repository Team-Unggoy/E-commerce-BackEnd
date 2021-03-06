from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('user-list/', views.UserList, name='user-list'),
    path('user-detail/<str:pk>/', views.UserDetail, name='user-detail'),
    path('user-create/', views.UserCreate, name='user-create'),

    path('login/', obtain_auth_token, name='login'),
    

]