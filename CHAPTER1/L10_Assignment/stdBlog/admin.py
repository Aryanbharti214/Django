from django.contrib import admin
from .models import Post
# Register your models here
# admin.site.register(Post)
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','publish','status']
    list_filter=['status','created','publish']
    prepopulated_fields={'slug':('title',)}#iske wajah se ek sath title aur slug same data type hota hai
    # raw_id_fields=['author']
    date_hierarchy='publish'
    ordering=['status','publish']
    show_facets=admin.ShowFacets.ALWAYS