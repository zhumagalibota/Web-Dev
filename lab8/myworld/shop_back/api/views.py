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