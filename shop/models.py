from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование товара')
    price = models.IntegerField(verbose_name='Цена товара')

    def __str__(self):
        return self.name


class Purchase(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО')
    age = models.IntegerField(verbose_name='Возраст')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='purchases')
    date_purchase = models.DateField(auto_now_add=True, verbose_name='Дата покупки')

    def __str__(self):
        return f'{self.name} - {self.age} - {self.item.name} - {self.date_purchase}'