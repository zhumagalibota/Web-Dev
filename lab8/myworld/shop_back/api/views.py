from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class ProductApiView(APIView):
    serializer_class = ProductSerializer
    def get(self, request):
        allProducts = Product.objects.all().values()
        return Response({"Message":"List of Products", "Product list":allProducts})

    def post(self, request):
        print('Requested data is: ', request.data)
        serializer_obj = ProductSerializer(data=request.data)
        if(serializer_obj.is_valid()):
            Product.objects.create(name=serializer_obj.data.get("name"),
                               price=serializer_obj.data.get("price"),
                               description=serializer_obj.data.get("description"),
                               count=serializer_obj.data.get("count"),
                               is_active=serializer_obj.data.get("is active")
                              )
        product = Product.objects.all().filter(name=request.data["name"]).values()
        return Response({"Message":"New product added", "Product":allProducts})

    def get_product(self, request):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

class CategoryApiView(APIView):
    serializer_class = CategorySerializer
    
    def get(self, request):
        allCategories = Category.objects.all().values()  # Corrected query here
        return Response({"Message": "List of Categories", "Category list": allCategories})

    def post(self, request):
        print('Requested data is: ', request.data)
        serializer_obj = CategorySerializer(data=request.data)
        if serializer_obj.is_valid():
            Category.objects.create(name=serializer_obj.data.get("name"))
        category = Category.objects.all().filter(name=request.data["name"]).values()
        return Response({"Message": "New category added", "Category": category})
