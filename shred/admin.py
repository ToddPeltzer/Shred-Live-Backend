from django.contrib import admin
from .models import Beach, Post, User

# Register your models here.

admin.site.register(Beach)
admin.site.register(Post)
admin.site.register(User)