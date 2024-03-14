from django.db import models


class Party(models.Model):
    class Meta:
        verbose_name_plural = 'Parties'

    name = models.CharField(max_length=100)
    initials = models.CharField(max_length=10)
    icon = models.ImageField(
        upload_to='product_images/%Y/%m/', blank=True, null=True)
    votes = models.IntegerField(default=0)
