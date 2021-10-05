# Generated by Django 3.2.7 on 2021-10-05 07:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('pk_no', models.AutoField(db_column='pno', primary_key=True, serialize=False)),
                ('order_no', models.CharField(db_column='order_no', max_length=14)),
                ('order_date', models.DateTimeField(db_column='order_date', default=datetime.datetime.now)),
                ('customer', models.CharField(db_column='customer', max_length=20)),
                ('customer_phone', models.CharField(db_column='customer_phone', max_length=11)),
                ('pay_check', models.CharField(db_column='pay_check', max_length=1)),
                ('order_type', models.ForeignKey(db_column='order_type', on_delete=django.db.models.deletion.CASCADE, related_name='order', to='information.order_type')),
                ('pay_type', models.ForeignKey(db_column='pay_type', on_delete=django.db.models.deletion.CASCADE, related_name='order', to='information.pay_type')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('order_item_no', models.AutoField(db_column='order_item_id', primary_key=True, serialize=False)),
                ('state', models.CharField(db_column='state', max_length=20)),
                ('receipt_date', models.DateTimeField(db_column='receipt_date')),
                ('phrase_option', models.CharField(db_column='phrase', max_length=1)),
                ('count', models.IntegerField(db_column='count')),
                ('total_price', models.IntegerField(db_column='total_price')),
                ('recipient', models.CharField(db_column='recipient', max_length=20)),
                ('recipient_phone', models.CharField(db_column='recipient_phone', max_length=11)),
                ('address', models.TextField(db_column='address')),
                ('memo', models.TextField(db_column='memo')),
                ('boxing_option', models.ForeignKey(db_column='boxing_id', on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='information.boxing')),
                ('delivery_option', models.ForeignKey(db_column='delivery_id', on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='information.delivery')),
                ('filling_option', models.ForeignKey(db_column='filling_id', on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='information.filling')),
                ('pk_no', models.ForeignKey(db_column='pk_no', on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='order_list.order')),
                ('product_id', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='information.product')),
                ('sheet_option', models.ForeignKey(db_column='sheet_id', on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='information.sheet')),
                ('size_option', models.ForeignKey(db_column='size_id', on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='information.size')),
            ],
            options={
                'db_table': 'order_item',
            },
        ),
    ]
