from django.urls import path
from . import views


urlpatterns = [
    path('user-list/', views.UserList, name='user-list'),
    path('user-detail/<str:pk>/', views.UserDetail, name='user-detail'),
    path('user-create/', views.UserCreate, name='user-create'),

]