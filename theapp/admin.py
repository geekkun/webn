from django.contrib import admin
from .models import Article, AppUser, Comments, Likes, Dislikes

# Register your models here.
admin.site.register(Article)
admin.site.register(AppUser)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Dislikes)

