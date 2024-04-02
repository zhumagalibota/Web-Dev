from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class ProductApiView(APIView):
    def get(self, request):
        allProducts = Product.objects.all().values()
        return Response({"Message":"List of Products", "Product list":allProducts})

    def post(self, request):
        Product.objects.create(name=request.data["name"],
                               price=request.data["price"],
                               description=request.data["description"],
                               count=request.data["count"],
                               is_active=request.data["is_active"]
                              )
        product = Product.objects.all().filter(name=request.data["name"]).values()
        return Response({"Message":"New product added", "Product":allProducts})