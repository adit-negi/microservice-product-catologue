from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .producer import *
from .models import *
import random
# Create your views here.


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        print('fasdfs')
        publish('product_list', {'id': 6})
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)  # check
        publish('product_created', serializer.data)
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
        publish('product_updated', serializer.data)
        return Response(serializer.data, status=202)

    def destroy(self, request, pk):
        try:
            product = Product.objects.get(pk=pk).delete()
        except:
            return Response(status=400)
        publish('product_deleted', pk)
        return Response(status=204)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id,
        })
