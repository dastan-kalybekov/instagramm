from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.post_list_create_api_view),
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroyApiView.as_view()),
    path('comments/', views.CommentListCreateApiView.as_view()),
    path('comments/<int:pk>/', views.CommentRetrieveUpdateDestroyApiView.as_view()),
]