from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        print(request.data)
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except:
            return Response(status=400)
        serializer = ProductSerializer(product, read_only=True)
        return Response(serializer.data, status=201)

    def update(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except:
            return Response(status=400)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=202)

    def destroy(self, request, pk):
        try:
            product = Product.objects.get(pk=pk).delete()
        except:
            return Response(status=400)
        return Response(status=204)
