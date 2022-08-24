from django.contrib import admin
from .models import Post,Photo
# Register your models here.
class PhotoInline(admin.TabularInline):
    model = Photo

# Post 클래스는 해당하는 Photo 객체를 리스트로 관리하는 한다. 
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]
    readonly_fields=('sell_date',)

# Register your models here.
admin.site.register(Post, PostAdmin)