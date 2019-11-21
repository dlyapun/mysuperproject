# Generated by Django 2.2.6 on 2019-11-18 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InstancePizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('count', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='MySuperModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=300, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('changed', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('first_name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('pizzas', models.ManyToManyField(blank=True, null=True, to='myAPP.InstancePizza')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='instancepizza',
            name='pizza_template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pizza_template', to='myAPP.Pizza'),
        ),
    ]
