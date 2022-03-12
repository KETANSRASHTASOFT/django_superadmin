from django.urls import path, include
from default import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers
# from default.views import SuperCategoryViewSet


router = routers.DefaultRouter()
router.register(r'website', views.WebSiteViewSet)
router.register(r'category_type', views.CategoryTypeViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'site_details', views.SiteDetailViewSet)

# router.register(r'super_category',SuperCategoryViewSet,basename='super_category')

urlpatterns = [
    path('', include(router.urls)),
    path('category_type_filter/',views.CategoryTypeFilter,name='category_type_filter'),
    path('category_filter/',views.CategoryFilter,name='category_filter'),
    path('sub_category_filter/',views.SubCategoryFilter,name='sub_category_filter'),
    path('product_filter/',views.ProductFilter,name='product_filter'),
    path('super_category/',views.SuperCategory,name='super_category'),
    
    
]