from django.core import validators
from django.db import models

from magazinslunce.common.validators import validate_file_size
# TODO: MAKE ACTUAL PRODUCTS

class Product(models.Model):
    PRODUCT_TYPE_MAX_LENGTH = 75
    PRODUCT_NAME_MAX_LENGTH = 75

    class Meta:
        ordering = ('-price',)

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