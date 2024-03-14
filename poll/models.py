from django.contrib.auth.models import User
from django.db import models


class Party(models.Model):
    class Meta:
        verbose_name_plural = 'Parties'

    name = models.CharField(max_length=100)
    initials = models.CharField(max_length=10)
    icon = models.ImageField(
        upload_to='product_images/%Y/%m/', blank=True, null=True)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=9)
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
