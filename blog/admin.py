from django.contrib import admin
from .models import Category,Post


#for config. of categogy admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','add_date','url',)
    search_fields = ('title',)
    


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields =('title',)
    list_filter = ('cat',)
    list_per_page = 50


    class Media:
        js = ('https://cdn.jsdelivr.net/npm/tinymce@6.6.2/tinymce.min.js','js/script.js',)





admin.site.register(Category,CategoryAdmin) 
admin.site.register(Post,PostAdmin)


