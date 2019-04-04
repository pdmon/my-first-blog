from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/modify/', views.modify, name='modify'),
    path('<int:post_id>/comment/', views.comment, name='comment'),
]
