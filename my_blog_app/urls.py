from django.urls import path, include
from .views import PostDetailView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path("", views.post_list, name='post_list'),
    path("myblogs", views.myblogs, name='my_blog'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

]