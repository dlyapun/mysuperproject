# Generated by Django 2.2.6 on 2019-11-18 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='f9405705ae2d48eb8d6539b4b9a6607390d67b493e224d43ae1ccecff3260fda', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='08af14d7316d4e6e91034d40cad96905411b0f8b33ea4fe2a2a0cd04e6dc3cc7', max_length=300, null=True),
        ),
    ]