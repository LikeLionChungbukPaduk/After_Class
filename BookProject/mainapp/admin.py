from django.contrib import admin
from .models import Post,PostImage

class PhotoAdmin(admin.StackedInline):
    model = PostImage
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoAdmin]

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)