from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model


User = get_user_model()


class Subcategory(models.Model):
    name = models.CharField(
        max_length=settings.NAME_MAX_LENGTH,
        unique=True,
        verbose_name='наименование'
    )
    slug = models.SlugField(
        max_length=settings.SLUG_MAX_LENGTH,
        verbose_name='Ссылка'
    )
    image = models.ImageField(
        upload_to='media/subcategory/images/',
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Category(models.Model):
    name = models.CharField(
        max_length=settings.NAME_MAX_LENGTH,
        unique=True,
        verbose_name='наименование'
    )
    slug = models.SlugField(
        max_length=settings.SLUG_MAX_LENGTH,
        verbose_name='Ссылка'
    )
    image = models.ImageField(
        upload_to='media/category/images/',
        blank=False,
        null=False,
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(
        max_length=settings.NAME_MAX_LENGTH,
        unique=True,
        verbose_name='наименование'
    )
    subcategory = models.ManyToManyField(
        Subcategory,
    )
    category = models.ManyToManyField(
        Category,
        related_name='product_category',
    )
    slug = models.SlugField(
        max_length=settings.SLUG_MAX_LENGTH,
        verbose_name='Ссылка'
    )
    image_first_size = models.ImageField(
        upload_to='media/product/image_first_size/',
        blank=False,
        null=False,
    )
    image_sec_size = models.ImageField(
        upload_to='media/product/image_sec_size/',
        blank=False,
        null=False,
    )
    image_trees_size = models.ImageField(
        upload_to='media/product/image_trees_size/',
        blank=False,
        null=False,
    )
    price = models.IntegerField(
        validators=[
            MinValueValidator(
                1,
                message='Минимальное цена 1р'
            ),
        ]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='+'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='is_in_shopping_cart',
    )

    class Meta:
        verbose_name = 'Cписок покупок'
        verbose_name_plural = 'Списки покупок'
