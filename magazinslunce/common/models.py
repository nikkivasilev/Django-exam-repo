from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from magazinslunce.products.models import Product

UserModel = get_user_model()


class ProductComment(models.Model):
    MAX_TEXT_LENGTH = 300

    class Meta:
        ordering = ["-publication_date_and_time"]

    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.product} - {self.user}: {self.publication_date_and_time}"


class ProductLike(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.product} - {self.user}"


class ProductRating(models.Model):
    rating = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ],
        null=False,
        blank=False,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.rating} : {self.product} - {self.user}"


class ProductBasket(models.Model):
    ordering = ('quantity',)

    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.product} - {self.user}"
