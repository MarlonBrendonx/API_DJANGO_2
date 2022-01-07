from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.showTest, name="show-teste"),
    path('user-list/', views.listUser, name="list-user"),
    path('user-detail/<str:pk>/', views.detailUser, name="detail-user"),
    path('user-create/', views.userCreate, name="user-create"),
    path('user-update/<str:pk>/', views.userUpdate, name="user-update"),
    path('user-delete/<str:pk>/', views.userDelete, name="user-delete"),
    path('users-export/', views.exportUsersxls, name="export-users")
]
