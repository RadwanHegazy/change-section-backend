from django.urls import path
from .views import get, create, delete


urlpatterns = [
    path('get/',get.GetPosts),
    path('create/',create.CreatePost),
    path('delete/<str:post_id>/',delete.DeletePost),
]