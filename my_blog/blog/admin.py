from django.contrib import admin
from .models import Post, Author, Tag, Comment
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # readonly_fields =  ("slug", )
    prepopulated_fields = {"slug":("title",)}
    list_filter = ("author","tag" ,"date")
    list_display = ("title", "date", "author")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)