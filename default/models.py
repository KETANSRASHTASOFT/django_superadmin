from django.db import models

# Create your models here.
class WebSite(models.Model):
    site_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=150)
    seo_url = models.CharField(max_length=255,blank =False,unique = True)
    short_details = models.CharField(max_length=800,blank = True)
    full_details = models.TextField(blank = True)
    site_icon = models.ImageField(upload_to='upload/sites/icon/',blank = True)
    site_logo = models.ImageField(upload_to='upload/sites/logo/',blank = True)
    site_image = models.ImageField(upload_to='upload/sites/image/',blank = True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)    
    def __str__(self):
        return self.name

class CategoryType(models.Model):
    categorytype_id = models.AutoField(primary_key = True)
    site_id = models.ForeignKey(WebSite, on_delete=models.CASCADE,null = True,blank = True)
    name = models.CharField(max_length=255,blank = False)
    seo_url = models.CharField(max_length=255,blank =False,unique = True)
    categorytype_image = models.ImageField(upload_to='upload/categorytype/image/',blank = True)
    is_active = models.BooleanField(default=True)    
    def __str__(self):
       return self.name

class Category(models.Model):
    category_id = models.AutoField(primary_key = True)
    site_id = models.ForeignKey(WebSite, on_delete=models.CASCADE,null = True,blank = True)
    categorytype_id = models.ForeignKey(CategoryType, on_delete=models.CASCADE,null = True,blank = True)
    name = models.CharField(max_length=150,blank = False)
    seo_url = models.CharField(max_length=255,blank =False,unique = True)
    short_details = models.CharField(max_length=800,blank = True)
    full_details = models.TextField(blank = True)
    category_icon = models.ImageField(upload_to='upload/category/icon/',blank = True)
    category_image = models.ImageField(upload_to='upload/category/image/',blank = True)
    category_cover_image = models.ImageField(upload_to='upload/category/cover_image/',blank = True)
    parent_id = models.ForeignKey("self", on_delete=models.CASCADE,null = True,blank = True,related_name = 'category_parent')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id = models.AutoField(primary_key = True)
    site_id = models.ForeignKey(WebSite, on_delete=models.CASCADE,null = True,blank = True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,null = True,blank = True)
    name = models.CharField(max_length=150,blank = False)
    short_details = models.CharField(max_length=800,blank = True)
    full_details = models.TextField(blank = True)
    product_image = models.ImageField(upload_to='upload/product/image/',blank = True)
    meta_data = models.CharField(max_length=255,blank=True)
    meta_image = models.ImageField(upload_to='upload/product/meta_image/',blank = True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class SiteDetail(models.Model):
    site_id = models.ForeignKey(WebSite, on_delete=models.CASCADE,null = True,blank = True)
    mobile_1 = models.CharField(max_length=12,blank = True)
    mobile_2 = models.CharField(max_length=12,blank = True)
    mobile_3 = models.CharField(max_length=12,blank = True)
    email_1 = models.EmailField(max_length=254,null = True,blank = True)
    email_2 = models.EmailField(max_length=254,null = True,blank = True)
    email_3 = models.EmailField(max_length=254,null = True,blank = True)
    address = models.TextField(blank = True)
    pincode = models.CharField(max_length=8,blank = True)
    image = models.ImageField(upload_to='upload/sites/header_logo/',blank = True)
    header_logo = models.ImageField(upload_to='upload/sites/header_logo/',blank = True)
    footer_logo = models.ImageField(upload_to='upload/sites/footer_logo/',blank = True)
    orther_logo = models.ImageField(upload_to='upload/sites/orther_logo/',blank = True)
    opposite_logo = models.ImageField(upload_to='upload/sites/opposite_logo/',blank = True)
    facebook_link = models.CharField(max_length=200,null = True,blank = True)
    instagram_link = models.CharField(max_length=200,null = True,blank = True)
    linkedin_link = models.CharField(max_length=200,null = True,blank = True)
    twitter_link = models.CharField(max_length=200,null = True,blank = True)
    pinterest_link = models.CharField(max_length=200,null = True,blank = True)
    map_link = models.CharField(max_length=800,null = True,blank = True)
    about_data = models.TextField(blank = True)
    vision_data = models.TextField(blank = True)
    mission_data = models.TextField(blank = True)
    termsandcondition = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
