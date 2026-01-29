from rest_framework import generics, filters
from .models import Product, Student
from .serializers import ProductSerializer, StudentSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ["name"]
    ordering_fields = ["price"]


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    search_fields = ["name", "phone"]
    ordering_fields = ["age"]


class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
