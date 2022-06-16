from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('delete-comment/<int:pk>/', views.CommentDeleteView.as_view(), name='delete_comment'),
]
