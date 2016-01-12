from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","timestamp","updated"]
    list_display_link = ["__unicode__"]
    list_filter=["timestamp", "updated"]
    #list_editable=[]
    search_fields=["content","title"]
    
    
    class Meta:
        model = Post
        
admin.site.register(Post, PostModelAdmin)