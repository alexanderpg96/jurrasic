"""Urls module for all url definitions in the API."""

from django.urls import path
from . import views

urlpatterns = [
    path("expense/", views.ExpenseListCreateView.as_view()),
    path("expense/<uuid:pk>/", views.ExpenseView.as_view()),
    path("category/", views.CategoryListCreateView.as_view()),
    path("category/<uuid:pk>/", views.CategoryView.as_view()),
    path("payment/", views.PaymentListCreateView.as_view()),
    path("payment/<uuid:pk>/", views.PaymentView.as_view()),
    path("category_forecast/", views.CategoryForecastListCreateView.as_view()),
    path("category_forecast/<uuid:pk>/", views.CategoryForecastView.as_view()),
]
