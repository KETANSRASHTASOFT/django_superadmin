from django.contrib import admin
from .models import WebSite,CategoryType,Category,Product,SiteDetail
# Register your models here.

class WebSiteAdmin(admin.ModelAdmin):
    list_display = ('site_id','name', 'seo_url', 'short_details')
    list_filter = ('name', 'seo_url')
admin.site.register(WebSite,WebSiteAdmin)

class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('categorytype_id','name', 'seo_url', )
    list_filter = ('site_id','name')
admin.site.register(CategoryType, CategoryTypeAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'seo_url', 'short_details')
    list_filter = ('site_id','name')
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('site_id','product_id','name', 'short_details')
    list_filter = ('site_id','name')
admin.site.register(Product, ProductAdmin)

class SiteDetailAdmin(admin.ModelAdmin):
    list_display = ('site_id','mobile_1', 'email_1', 'address')
    list_filter = ('site_id','mobile_1')
admin.site.register(SiteDetail, SiteDetailAdmin)
