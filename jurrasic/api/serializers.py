"""Serializers module for all serializers in the API."""

from rest_framework import serializers
from api import models


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the category object in the database."""

    class Meta:
        model = models.Category
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    """Serializer for the payment object in the database."""

    class Meta:
        model = models.Payment
        fields = "__all__"


class CategoryForecastSerializer(serializers.ModelSerializer):
    """Serializer for the category_forecast object in the database."""

    class Meta:
        model = models.CategoryForecast
        fields = "__all__"

    def to_representation(self, instance):
        """Modify the response json to represent category objects (instead of just their uuid's).

        Args:
            instance (CategoryForecaseSerializer): CategoryForecaseSerializer instance

        Returns:
            CategoryForecaseSerializer: Updated serializer representation
        """
        self.fields["category"] = CategorySerializer(read_only=True)
        return super(CategoryForecastSerializer, self).to_representation(instance)


class ExpenseSerializer(serializers.ModelSerializer):
    """Serializer for the expense object in the database."""

    class Meta:
        model = models.Expense
        fields = "__all__"

    def to_representation(self, instance):
        """Modify the response json to represent category and payment objects (instead of just their uuid's).

        Args:
            instance (ExpenseSerializer): ExpenseSerializer instance

        Returns:
            ExpenseSerializer: Updated serializer representation
        """
        self.fields["category"] = CategorySerializer(read_only=True)
        self.fields["payment"] = PaymentSerializer(read_only=True)
        return super(ExpenseSerializer, self).to_representation(instance)
