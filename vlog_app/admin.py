from django.contrib import admin
from .models import Post, Contact, SiteInfo


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_draft',
        'is_delete',
        'create_date',
        'update_date',
        'user_id'
    )
    list_filter = filter = ('is_draft', 'is_delete')
    
    search_fields = (
        'title',
        'description',
        'user_id__username'
    )
    ordering = ('-create_date',)


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_active',
        'create_date',
        'update_date'
    )
    list_filter = ('is_active',)
    
    ordering = ('-create_date',)


class SiteInfoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_active',
        'create_date',
        'update_date'
    )
    list_filter = ('is_active',)
    
    ordering = ('-create_date',)


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(SiteInfo, SiteInfoAdmin)