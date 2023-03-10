# Generated by Django 4.1.5 on 2023-01-29 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.TextField(verbose_name='Фамилия')),
                ('name', models.TextField(verbose_name='Имя')),
                ('middlename', models.TextField(verbose_name='Отчество')),
                ('telephone', models.TextField(max_length=12, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'permissions': (('admin_permission', 'admin permission'),),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.TextField(verbose_name='Фамилия')),
                ('name', models.TextField(verbose_name='Имя')),
                ('middlename', models.TextField(verbose_name='Отчество')),
                ('job_title', models.TextField(verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'permissions': (('admin_permission', 'admin permission'),),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=512, unique=True, verbose_name='Адрес')),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saidapp.employee')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
                'permissions': (('admin_permission', 'admin permission'),),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Товар')),
                ('task', models.TextField(max_length=512, verbose_name='Описание товара')),
                ('price', models.IntegerField(verbose_name='Цена товара')),
                ('distributor', models.TextField(verbose_name='Поставщик')),
                ('type_good', models.TextField(verbose_name='Тип товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'permissions': (('admin_permission', 'admin permission'),),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery', models.BooleanField(verbose_name='Доставка')),
                ('date_order', models.DateTimeField(verbose_name='Дата заказа')),
                ('payment', models.TextField(verbose_name='Метод оплаты')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saidapp.market', to_field='address')),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saidapp.employee')),
                ('idClient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saidapp.client')),
                ('product_deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saidapp.product')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'permissions': (('admin_permission', 'admin permission'),),
                'managed': True,
            },
        ),
    ]
