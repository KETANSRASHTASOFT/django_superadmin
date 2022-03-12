from rest_framework import serializers

from default.models import WebSite,CategoryType,Category,Product,SiteDetail


# rest framework defalut
class WebSiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WebSite
        fields = "__all__"

class CategoryTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoryType
        fields = "__all__"

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class SiteDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SiteDetail
        fields = "__all__"



# custome model serialize

class CategoryTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryType
        fields = "__all__"


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class Sub3SuperCategorySerializer(serializers.ModelSerializer):
    # sub_category = Sub3SuperCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = "__all__"

class Sub2SuperCategorySerializer(serializers.ModelSerializer):
    sub_category = Sub3SuperCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = "__all__"

class SubSuperCategorySerializer(serializers.ModelSerializer):
    sub_category = Sub2SuperCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = "__all__"

class SuperCategorySerializer(serializers.ModelSerializer):
    sub_category = SubSuperCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = "__all__"