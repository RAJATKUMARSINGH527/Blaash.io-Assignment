from django.urls import path
from .views import RegisterView, LoginView, PostCreateView, PostListView, CommentCreateView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/posts/', PostListView.as_view(), name='post-list'),
    path('api/posts/create/', PostCreateView.as_view(), name='post-create'),
    path('api/posts/comments/', CommentCreateView.as_view(), name='comment-create'),
]