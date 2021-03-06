from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('register/do/', views.register_do, name='register_do'),
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/modify/', views.modify, name='modify'),
    path('<int:post_id>/comment/', views.comment, name='comment'),
    path('<int:post_id>/remove/', views.remove, name='remove'),
]
