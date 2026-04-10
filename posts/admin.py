from django.contrib import admin

from posts.models import Post, Tags

admin.site.register(Post)

admin.site.register(Tags)
