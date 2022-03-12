from django.shortcuts import render
from rest_framework import viewsets
from default.serializers import (WebSiteSerializer,CategoryTypeSerializer,CategorySerializer,ProductSerializer,SiteDetailSerializer,CategoryTypeModelSerializer,CategoryModelSerializer,ProductModelSerializer,SuperCategorySerializer)
from default.models import WebSite,CategoryType, Category, Product, SiteDetail


# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# Create your views here.

class WebSiteViewSet(viewsets.ModelViewSet):
    queryset = WebSite.objects.all()
    serializer_class = WebSiteSerializer

class CategoryTypeViewSet(viewsets.ModelViewSet):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SiteDetailViewSet(viewsets.ModelViewSet):
    queryset = SiteDetail.objects.all()
    serializer_class = SiteDetailSerializer

    # ####  **** FOR SINGALE PERAMITER ****  ####
        # from rest_framework.response import Response
        # class SuperCategoryViewSetdemo(viewsets.ViewSet):
        #     def list(self, request):
        #         queryset = Category.objects.all()
        #         serializer = CategorySerializer(queryset, many=True)
        #         print("************* LIST *******************")
        #         print(serializer.__dict__)
        #         print("************* END LIST *******************")
        #         return Response(serializer.data)

        #     def retrieve(self, request, pk=None):
        #         category = Category.objects.filter(site_id=pk)
        #         serializer = CategorySerializer(category, many=True)
        #         print("************* retrieve *******************")
        #         print(serializer.__dict__)
        #         print("************* END retrieve *******************")
                
        #         return Response(serializer.data)

        #     def get_queryset(self):
        #         site_id = self.request.site_id
        #         print("************* get_queryset *******************")
        #         print(serializer)
        #         print("************* END get_queryset *******************")
        #         return Category.objects.filter(site_id=site_id)

from django.db.models import Q, F  #
from rest_framework.decorators import api_view
from django.http import  JsonResponse #HttpResponse,


@api_view(["POST"])
def CategoryTypeFilter(request):
    if request.method == "POST":
        query = Q()
        if 'site_id' in request.POST:
            query = query & Q(site_id=request.POST['site_id'])
        if 'categorytype_id' in request.POST:
            query = query & Q(categorytype_id=request.POST['categorytype_id'])

        categorytype = CategoryType.objects.filter(query)

        categorytype_serializer = CategoryTypeModelSerializer(categorytype, many=True)
        return JsonResponse(categorytype_serializer.data, safe=False)


@api_view(["POST"])
def CategoryFilter(request):
    if request.method == "POST":
        query = Q()
        query = query & Q(parent_id=None)
        if 'site_id' in request.POST:
            query = query & Q(site_id=request.POST['site_id'])
        if 'categorytype_id' in request.POST:
            query = query & Q(categorytype_id=request.POST['categorytype_id'])
        if 'category_id' in request.POST:
            query = query & Q(category_id=request.POST['category_id'])

        category = Category.objects.filter(query)

        category_serializer = CategoryModelSerializer(category, many=True)
        return JsonResponse(category_serializer.data, safe=False)

@api_view(["POST"])
def SubCategoryFilter(request):
    if request.method == "POST":
        query = Q()
        if 'category_id' in request.POST:
            query = query & Q(parent_id=request.POST['category_id'])

        category = Category.objects.filter(query)

        category_serializer = CategoryModelSerializer(category, many=True)
        return JsonResponse(category_serializer.data, safe=False)

@api_view(["POST"])
def ProductFilter(request):
    if request.method == "POST":
        query = Q()
        if 'site_id' in request.POST:
            query = query & Q(site_id=request.POST['site_id'])
        if 'categorytype_id' in request.POST:
            query = query & Q(category_id__categorytype_id=request.POST['categorytype_id'])
        if 'category_id' in request.POST:
            query = query & Q(category_id=request.POST['category_id'])

        product = Product.objects.filter(query)

        product_serializer = ProductModelSerializer(product, many=True)
        return JsonResponse(product_serializer.data, safe=False)

from django.db.models import  Prefetch #Count
@api_view(["POST"])
def SuperCategory(request):
    query = Q()
    query = query & Q(parent_id=None)
    if 'site_id' in request.POST:
        query = query & Q(site_id=request.POST['site_id'])
    if 'categorytype_id' in request.POST:
        query = query & Q(categorytype_id=request.POST['categorytype_id'])
    if 'category_id' in request.POST:
        query = query & Q(category_id=request.POST['category_id'])

    category = Category.objects.filter(query).select_related("parent_id").prefetch_related(Prefetch(
        'category_parent',queryset=Category.objects.filter(parent_id=F("parent_id")).select_related("parent_id").prefetch_related(Prefetch('category_parent',
            queryset=Category.objects.filter(parent_id=F("parent_id")).select_related("parent_id").prefetch_related(Prefetch('category_parent',
            queryset=Category.objects.filter(parent_id=F("parent_id")),
            to_attr="sub_category")
        ),
            to_attr="sub_category")
        ),
        to_attr='sub_category')
    )

    category_serializer = SuperCategorySerializer(category, many=True)
    return JsonResponse(category_serializer.data, safe=False)