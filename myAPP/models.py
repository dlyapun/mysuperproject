from django.db import models

# Create your models here.
class MySuperModel(models.Model):
    token = models.CharField(max_length=300, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    changed = models.BooleanField(default=False)
    name = models.CharField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    first_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return 'MySuperModel'

    def __check_field__(self):
        return self.name
