from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class product(models.Model):
    title = models.CharField('Товар', max_length=200)
    task = models.TextField('Описание товара', max_length=512)
    price = models.IntegerField('Цена товара')
    distributor = models.TextField('Поставщик')
    type_good = models.TextField('Тип товара')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/products'

    class Meta:
        managed = True
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        permissions = (("admin_permission", "admin permission"),)

class Employee(models.Model):
    surname = models.TextField('Фамилия')
    name = models.TextField('Имя')
    middlename = models.TextField('Отчество')
    job_title = models.TextField('Должность')

    def __str__(self):
        return "%s %s %s" % (self.surname, self.name, self.middlename)


    def get_absolute_url(self):
        return f'/employee'

    class Meta:
        managed = True
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        permissions = (("admin_permission", "admin permission"),)

class Market(models.Model):
    address = models.TextField('Адрес', max_length=512, unique=True)
    admin_id = models.ForeignKey(Employee, to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return f'/markets'

    class Meta:
        managed = True
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        permissions = (("admin_permission", "admin permission"),)

class Client(models.Model):
    surname = models.TextField('Фамилия')
    name = models.TextField('Имя')
    middlename = models.TextField('Отчество')
    telephone = models.TextField('Номер телефона', max_length=12)

    def __str__(self):
        return "%s %s %s" % (self.surname, self.name, self.middlename)

    class Meta:
        managed = True
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        permissions = (("admin_permission", "admin permission"),)

class Order(models.Model):
    product_deal = models.ForeignKey(product, to_field='id', on_delete=models.CASCADE)
    delivery = models.BooleanField('Доставка')
    address = models.ForeignKey(Market, to_field='address', on_delete=models.CASCADE)
    date_order = models.DateTimeField('Дата заказа')
    idClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    payment = models.TextField('Метод оплаты')
    admin_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.product_deal, self.idClient)

    class Meta:
        managed = True
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        permissions = (("admin_permission", "admin permission"),)

