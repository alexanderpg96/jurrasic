# Generated by Django 4.0.1 on 2022-01-18 22:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=999)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('created_by', models.UUIDField()),
                ('last_modified', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_by', models.UUIDField()),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=999)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('created_by', models.UUIDField()),
                ('last_modified', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_by', models.UUIDField()),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=999)),
                ('ammount', models.FloatField()),
                ('date_of_expense', models.DateTimeField()),
                ('is_income', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('created_by', models.UUIDField()),
                ('last_modified', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_by', models.UUIDField()),
                ('category', models.ForeignKey(db_column='category_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.category')),
                ('payment', models.ForeignKey(db_column='payment_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.payment')),
            ],
            options={
                'db_table': 'expense',
                'ordering': ['date_of_expense'],
            },
        ),
        migrations.CreateModel(
            name='CategoryForecast',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ammount', models.FloatField()),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('created_by', models.UUIDField()),
                ('last_modified', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_by', models.UUIDField()),
                ('category', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='api.category')),
            ],
            options={
                'db_table': 'category_forecast',
            },
        ),
    ]
