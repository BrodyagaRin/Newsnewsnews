from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Post, Author, Comment


def home_view(request):
    posts = Post.objects.all().prefetch_related('author', 'categories')

    best_user = Author.objects.order_by('-rating').first()
    best_user_instance = best_user.user if best_user else None

    best_post = Post.objects.order_by('-rating').first()
    comments = Comment.objects.filter(post=best_post) if best_post else []

    context = {
        'posts': posts,
        'best_user': best_user_instance,
        'best_post': best_post,
        'comments': comments,
    }
    return render(request, 'home.html', context)


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like()
    return redirect('home')


def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.dislike()
    return redirect('home')


def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.like()
    return redirect('home')


def dislike_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.dislike()
    return redirect('home')
def create_authors(request):
    users = User.objects.all()

    for user in users:
        author, created = Author.objects.get_or_create(user=user)
        if created:
            print(f"Created author for user: {user.username}")
        else:
            print(f"Author already exists for user: {user.username}")

    return HttpResponse("Authors have been created or already exist.")


def create_comments(request):
    users = User.objects.all()[:4]
    posts = Post.objects.all()[:4]


    for i, post in enumerate(posts):
        user = users[i % len(users)]
        Comment.objects.create(
            post=post,
            user=user,
            text=f'Comments for post {post.title} from {user.username}',
            rating=0
        )

    return HttpResponse("Comments are created.")

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Comment
from django.contrib.auth.models import User

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.like()
    return redirect('home')

def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.dislike()
    return redirect('home')

def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.like()
    return redirect('home')

def dislike_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.dislike()
    return redirect('home')