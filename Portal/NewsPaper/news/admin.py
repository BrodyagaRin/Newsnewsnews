from django.contrib import admin
from .models import Author, Category, Post, Comment

admin.site.register(Author)
admin.site.register(Comment)

class PostCategoryInline(admin.TabularInline):
    model = Post.categories.through
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInline]
    list_display = ('title', 'author', 'created_at', 'rating')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
