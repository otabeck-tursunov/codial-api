from django.contrib import admin
from django.urls import path

from main.views import (
    ProductListCreateAPIView, ProductDetailAPIView,
    StudentListCreateAPIView, StudentDetailAPIView
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Mini API",
        default_version="v1",
        description="Product & Student CRUD API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
    path("products/", ProductListCreateAPIView.as_view()),
    path("products/<int:pk>/", ProductDetailAPIView.as_view()),

    path("students/", StudentListCreateAPIView.as_view()),
    path("students/<int:pk>/", StudentDetailAPIView.as_view()),
]
