from django.contrib import admin

# Register your models here.
from .models import Comment,Post
# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','publish','status']
    list_filter=['status','created','publish','author']
    prepopulated_fields={'slug':('title',)}#iske wajah se ek sath title aur slug same data type hota hai
    raw_id_fields=['author']
    date_hierarchy='publish'
    ordering=['status','publish']
    show_facets=admin.ShowFacets.ALWAYS
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']