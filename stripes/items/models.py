from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.PositiveIntegerField(verbose_name="Цена")
    currency = models.CharField(
        max_length=3,
        default='usd',
        verbose_name='Валюта'
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=50, verbose_name='Вид налога')
    percentage = models.FloatField(verbose_name='Размер Налога')

    class Meta:
        verbose_name = "Налог"
        verbose_name_plural = "Налоги"

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=50, verbose_name='Вид скидки')
    percentage = models.FloatField(verbose_name='Размер скидки')

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item, verbose_name='Товар')
    tax = models.ForeignKey(
        Tax,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Налог'
    )
    discount = models.ForeignKey(
        Discount,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Скидка'
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
