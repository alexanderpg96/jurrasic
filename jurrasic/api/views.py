"""Views module for all endpoints in API."""

import uuid
from django.db.models import Sum
from django.forms.models import model_to_dict

from api import models
from api import serializers
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime


class ExpenseListCreateView(generics.ListCreateAPIView):
    """API View for listing and creating expense objects in the database."""

    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer
    filterset_fields = ["is_income"]
    pagination_class = None

    def get_queryset(self):
        if self.request.query_params.get("start_date"):
            start_date = self.request.query_params.get("start_date")
            end_date = self.request.query_params.get("end_date")

            queryset = models.Expense.objects.filter(
                date_of_expense__range=[start_date, end_date]
            )

            if self.request.query_params.get("limit"):
                queryset = queryset[: int(self.request.query_params.get("limit"))]

            return queryset.order_by("-date_of_expense")

        return super().get_queryset()

    def create(self, request, format=None):
        if type(request.data) == list:
            for expense in request.data:
                expense["created_by"] = uuid.UUID(
                    "1124be7a-fbb9-4a66-a46c-2a5f6aea3833"
                )
                expense["updated_by"] = uuid.UUID(
                    "1124be7a-fbb9-4a66-a46c-2a5f6aea3833"
                )
                serializer = serializers.ExpenseSerializer(data=expense)

                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST, data=serializer.errors
                    )

            return Response(status=status.HTTP_201_CREATED, data={})
        else:
            request.data["created_by"] = uuid.UUID(
                "1124be7a-fbb9-4a66-a46c-2a5f6aea3833"
            )
            request.data["updated_by"] = uuid.UUID(
                "1124be7a-fbb9-4a66-a46c-2a5f6aea3833"
            )
            super().create(request)


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


class CategoryForecastCreateView(generics.CreateAPIView):
    """API View for creating category_forecast objects in the database."""

    queryset = models.CategoryForecast.objects.all()
    serializer_class = serializers.CategoryForecastSerializer
    pagination_class = None


class CategoryForecastApiView(APIView):
    """API View for listing category_forecast objects in the database in relation to their progress."""

    def get(self, request, format=None):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")
        user_id = uuid.UUID("1124be7a-fbb9-4a66-a46c-2a5f6aea3833")

        category_forecasts = models.CategoryForecast.objects.filter(created_by=user_id)
        expenses = models.Expense.objects.filter(
            date_of_expense__range=[start_date, end_date],
            created_by=user_id,
            is_income=False,
        )

        forecasts = []

        for forecast in category_forecasts:
            print(expenses.filter(category=forecast.category))

            forecasts.append(
                {
                    "category": forecast.category.name,
                    "forecast": forecast.ammount,
                    "expenses": expenses.filter(
                        category=forecast.category.id
                    ).aggregate(Sum("ammount"))["ammount__sum"],
                }
            )

        return Response(status=status.HTTP_200_OK, data=forecasts)

    def post(self, request, format=None):
        serializer = serializers.CategoryForecastSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.validated_data)
            validated_data = serializer.validated_data
            validated_data["category"] = model_to_dict(validated_data["category"])
            return Response(status=status.HTTP_201_CREATED, data=validated_data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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
