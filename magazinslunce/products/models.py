from django.core import validators
from django.db import models

from magazinslunce.common.validators import validate_file_size


class Product(models.Model):
    PRODUCT_TYPE_MAX_LENGTH = 75
    PRODUCT_NAME_MAX_LENGTH = 75

    class Meta:
        ordering = ('type',)

    name = models.CharField(
        max_length=PRODUCT_NAME_MAX_LENGTH,
        null=False,
        blank=False,
    )

    type = models.CharField(
        max_length=PRODUCT_TYPE_MAX_LENGTH,
        blank=False,
        null=False
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    Image = models.ImageField(
        upload_to='product_pictures',
        validators=[validate_file_size],
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=[
            validators.MinValueValidator(limit_value=0)
        ],
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.name} - {self.type}'
