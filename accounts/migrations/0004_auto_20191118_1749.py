# Generated by Django 2.2.6 on 2019-11-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191118_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='6eb1a4bcb05946a09b3e97bc242260b171409b296a584f2988de71426781e115', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='be66a366f24b4d21b78469d5fcacf2f3f110dcbfd5774ef394aadc978f3ff519', max_length=300, null=True),
        ),
    ]