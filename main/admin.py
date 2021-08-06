from django.contrib import admin
from .models import Post
from client.models import User




class PostAdmin(admin.ModelAdmin):
    list_display=[
        'user_id',
        'id',
        'subject',
        'content',
        'video',
        'added_at'
    ]
    list_display_links=[
        'subject'
    ]
    class Meta:
        model=Post

admin.site.register(Post,PostAdmin)



