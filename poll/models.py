import os

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from PIL import Image


class Party(models.Model):
    class Meta:
        verbose_name_plural = 'Parties'

    name = models.CharField(max_length=100)
    initials = models.CharField(max_length=10)
    icon = models.ImageField(
        upload_to='product_images/%Y/%m/', blank=True, null=True)
    votes = models.IntegerField(default=0)

    @staticmethod
    def resize_image(img, new_width=300):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=9, unique=True)
    date_of_birth = models.DateField()
    region = models.CharField(
        max_length=2,
        choices=(
            ('AV', 'Aveiro'),
            ('BE', 'Beja'),
            ('BG', 'Braga'),
            ('BN', 'Bragança'),
            ('CB', 'Castelo Branco'),
            ('CO', 'Coimbra'),
            ('EV', 'Évora'),
            ('FA', 'Faro'),
            ('GU', 'Guarda'),
            ('LE', 'Leiria'),
            ('LX', 'Lisboa'),
            ('PG', 'Portalegre'),
            ('PO', 'Porto'),
            ('SA', 'Santarém'),
            ('SE', 'Setúbal'),
            ('VC', 'Viana do Castelo'),
            ('VR', 'Vila Real'),
            ('VS', 'Viseu'),
            ('AC', 'Açores'),
            ('MA', 'Madeira'),
            ('EU', 'Outros países da Europa'),
            ('FE', 'Outros países fora da Europa'),
        )
    )

    def __str__(self) -> str:
        return self.full_name


class Vote(models.Model):
    voter = models.ForeignKey(Profile, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
