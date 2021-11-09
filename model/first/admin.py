from django.contrib import admin

from .models import *
from django.utils.html import format_html

class Blogadmin(admin.ModelAdmin):
    #fields=('title',)
    exclude=('is_deleted',)
    readonly_fields=['photo_tag',]
    list_display=('title','less_content','photo_tag','is_deleted','click_me','extra_title',)
    list_display_links=('less_content','title',)
    radio_fields={"tags":admin.HORIZONTAL}
    
    list_filter=('is_deleted','created_at',('extra_title',admin.EmptyFieldListFilter))
    save_on_top=True
    list_per_page=2
    def less_content(self,obj):
        return format_html(f'<span style="color:green">{obj.content[:30]}</span>')
    def click_me(self,obj):
       
        return format_html(f'<a href="/admin/first/blog/{obj.id}/change/" class="default">View</a>')
    def photo_tag(self,obj):
        return format_html(f'<img src="/media/{obj.image}" style="height:100px;width:100px">')

admin.site.register(Blog,Blogadmin)
