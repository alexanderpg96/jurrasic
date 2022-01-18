"""Views module for all endpoints in API."""

from django.shortcuts import render

from api import models
from api import serializers
from rest_framework import generics
from datetime import datetime


class ExpenseListCreateView(generics.ListCreateAPIView):
    """API View for listing and creating expense objects in the database."""

    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer


class ExpenseView(generics.RetrieveUpdateDestroyAPIView):
    """API View for retrieval, update, or destroy of an expense object in the database."""

    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer

    def perform_update(self, serializer):
        serializer.save(last_modified=datetime.now())
        return super().perform_update(serializer)


class CategoryListCreateView(generics.ListCreateAPIView):
    """API View for listing and creating category objects in the database."""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class = None


class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    """API View for retrieval, update, or destroy of a category object in the database."""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def perform_update(self, serializer):
        serializer.save(last_modified=datetime.now())
        return super().perform_update(serializer)


class CategoryForecastListCreateView(generics.ListCreateAPIView):
    """API View for listing and creating category_forecast objects in the database."""

    queryset = models.CategoryForecast.objects.all()
    serializer_class = serializers.CategoryForecastSerializer
    pagination_class = None


class CategoryForecastView(generics.RetrieveUpdateDestroyAPIView):
    """API View for retrieval, update, or destroy of a category_forecast object in the database."""

    queryset = models.CategoryForecast.objects.all()
    serializer_class = serializers.CategoryForecastSerializer

    def perform_update(self, serializer):
        serializer.save(last_modified=datetime.now())
        return super().perform_update(serializer)


class PaymentListCreateView(generics.ListCreateAPIView):
    """API View for listing and creating payment objects in the database."""

    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer
    pagination_class = None


class PaymentView(generics.RetrieveUpdateDestroyAPIView):
    """API View for retrieval, update, or destroy of a payment object in the database."""

    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

    def perform_update(self, serializer):
        serializer.save(last_modified=datetime.now())
        return super().perform_update(serializer)
