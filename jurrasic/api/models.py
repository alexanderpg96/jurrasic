"""Models module for all database table definitions."""

from datetime import datetime
from django.db import models
import uuid
from datetime import datetime


class Category(models.Model):
    """Category object model.

    This model represents all expense categories that a user has created
    for themselves. Users can create as many categories as they would like to have.

    DB Table: category
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=999)
    date_created = models.DateTimeField(default=datetime.now)
    created_by = models.UUIDField()
    last_modified = models.DateTimeField(default=datetime.now)
    updated_by = models.UUIDField()

    class Meta:
        db_table = "category"


class CategoryForecast(models.Model):
    """CategoryForecast object model.

    This model represents all expense forecasts that a user has created
    for themselves. Users can create as many category forecasts as they would like
    to have.

    DB Table: category_forecast
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ammount = models.FloatField()
    category = models.ForeignKey(
        to=Category, db_column="category_id", on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(default=datetime.now)
    created_by = models.UUIDField()
    last_modified = models.DateTimeField(default=datetime.now)
    updated_by = models.UUIDField()

    class Meta:
        db_table = "category_forecast"


class Payment(models.Model):
    """Payment object model.

    This model represents all payment types that a user has created for themselves.
    Users can create as many payment types as they would like.

    Examples include a Visa Card, Discover Card, etc.

    DB Table: payment
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=999)
    date_created = models.DateTimeField(default=datetime.now)
    created_by = models.UUIDField()
    last_modified = models.DateTimeField(default=datetime.now)
    updated_by = models.UUIDField()

    class Meta:
        db_table = "payment"


class Expense(models.Model):
    """Expense object model.

    This model represents all expenses that a user has incurred. These expenses
    can either be deductions or incomes.

    Examples include paying for groceries, or getting paid for a job.

    DB Table: expense
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=999)
    ammount = models.FloatField()
    date_of_expense = models.DateTimeField()
    is_income = models.BooleanField(default=False)
    category = models.ForeignKey(
        to=Category, db_column="category_id", on_delete=models.SET_NULL, null=True
    )
    payment = models.ForeignKey(
        to=Payment, db_column="payment_id", on_delete=models.SET_NULL, null=True
    )
    date_created = models.DateTimeField(default=datetime.now)
    created_by = models.UUIDField()
    last_modified = models.DateTimeField(default=datetime.now)
    updated_by = models.UUIDField()

    class Meta:
        db_table = "expense"
        ordering = ["date_of_expense"]
