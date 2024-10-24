from django.urls import path
from .views import home_view, like_post, dislike_post, like_comment, dislike_comment

urlpatterns = [
    path('', home_view, name='home'),
    path('post/<int:post_id>/like/', like_post, name='like_post'),
    path('post/<int:post_id>/dislike/', dislike_post, name='dislike_post'),
    path('comment/<int:comment_id>/like/', like_comment, name='like_comment'),
    path('comment/<int:comment_id>/dislike/', dislike_comment, name='dislike_comment'),
]