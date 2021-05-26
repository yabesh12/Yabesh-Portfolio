from django.contrib import admin

from . models import Post, Tag, Signup
# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)

admin.site.register(Signup)
