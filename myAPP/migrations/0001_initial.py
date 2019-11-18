# Generated by Django 2.2.6 on 2019-11-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MySuperModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=300, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('changed', models.BooleanField(default=False)),
            ],
        ),
    ]
