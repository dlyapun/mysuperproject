# Generated by Django 2.2.6 on 2019-11-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20191118_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='cd49c8fc2930456ba3752b96da37998d38d1522230e147cfb530bb36995bbe5b', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='d7160992a1ee4f6d9b117a03f83322dd135285e7ad23480199c3171e30ebc50e', max_length=300, null=True),
        ),
    ]
