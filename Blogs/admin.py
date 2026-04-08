from django.contrib import admin
from .models import Category

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'status', 'featured_post', 'created_at', 'category')
    search_fields = ('title', 'category__name', 'author__username', 'status')
    list_editable = ('status', 'featured_post', 'author', 'category')
from .models import Blog
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)


