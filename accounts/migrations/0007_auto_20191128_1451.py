# Generated by Django 2.2.6 on 2019-11-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191118_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='917f73787f8c434397d133a8d577a1b63e408d25afe444a5a2ee598ef1d7e49a', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='db7492c1fe604bcd859ff53f74aec75d76a895e00f7f428382763aafa0d1521a', max_length=300, null=True),
        ),
    ]
