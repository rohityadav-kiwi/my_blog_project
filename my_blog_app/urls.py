from django.urls import path, include
from .views import PostDetailView
from . import views

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path("", views.post_list, name='post_list'),
    path("random_string", views.random_number, name='random'),

]