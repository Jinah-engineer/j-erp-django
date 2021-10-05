# Generated by Django 3.2.7 on 2021-10-04 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boxing',
            fields=[
                ('boxing_id', models.AutoField(db_column='boxing_id', primary_key=True, serialize=False)),
                ('boxing_name', models.CharField(db_column='boxing_name', max_length=50)),
                ('boxing_price', models.IntegerField(db_column='boxing_price', default=0)),
            ],
            options={
                'db_table': 'boxing',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(db_column='category_id', primary_key=True, serialize=False)),
                ('category_big', models.CharField(db_column='category_big', max_length=50)),
                ('category_mid', models.CharField(db_column='category_mid', max_length=50)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.AutoField(db_column='delivery_id', primary_key=True, serialize=False)),
                ('delivery_name', models.CharField(db_column='delivery_name', max_length=50)),
            ],
            options={
                'db_table': 'delivery',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(db_column='employee_id', primary_key=True, serialize=False)),
                ('employee_name', models.CharField(db_column='employee_name', max_length=255)),
                ('employee_rank', models.CharField(db_column='employee_rank', max_length=50)),
                ('hiredate', models.DateTimeField(db_column='hiredate')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Filling',
            fields=[
                ('filling_id', models.AutoField(db_column='filling_id', primary_key=True, serialize=False)),
                ('filling_name', models.CharField(db_column='filling_name', max_length=50)),
                ('filling_price', models.IntegerField(db_column='filling_price', default=0)),
            ],
            options={
                'db_table': 'filling',
            },
        ),
        migrations.CreateModel(
            name='Order_type',
            fields=[
                ('order_type_id', models.AutoField(db_column='order_type_id', primary_key=True, serialize=False)),
                ('order_type_name', models.CharField(db_column='order_type_name', max_length=50)),
            ],
            options={
                'db_table': 'order_type',
            },
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('pay_id', models.AutoField(db_column='pay_id', primary_key=True, serialize=False)),
                ('pay_name', models.CharField(db_column='pay_name', max_length=50)),
            ],
            options={
                'db_table': 'pay',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(db_column='product_id', primary_key=True, serialize=False)),
                ('product_name', models.CharField(db_column='product_name', max_length=255)),
                ('product_price', models.IntegerField(db_column='product_price', default=0)),
                ('category_id', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, related_name='product', to='information.category')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('sheet_id', models.AutoField(db_column='sheet_id', primary_key=True, serialize=False)),
                ('sheet_name', models.CharField(db_column='sheet_name', max_length=50)),
                ('sheet_price', models.IntegerField(db_column='sheet_price', default=0)),
            ],
            options={
                'db_table': 'sheet',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('size_id', models.AutoField(db_column='size_id', primary_key=True, serialize=False)),
                ('size_name', models.CharField(db_column='size_name', max_length=50)),
                ('size_price', models.IntegerField(db_column='size_price', default=0)),
                ('product_id', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, related_name='size', to='information.product')),
            ],
            options={
                'db_table': 'size',
            },
        ),
    ]
