from django.contrib import admin
from .models import Article, AppUser, Comments

# Register your models here.
admin.site.register(Article)
admin.site.register(AppUser)
admin.site.register(Comments)

