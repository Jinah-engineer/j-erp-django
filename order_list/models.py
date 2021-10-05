from django.db import models
from information import models as information_models
from datetime import datetime
# Create your models here.


class Order(models.Model):
    pk_no = models.AutoField(db_column='pno', primary_key=True)
    order_no = models.CharField(db_column='order_no', max_length=14)
    order_date = models.DateTimeField(db_column='order_date', default=datetime.now)
    customer = models.CharField(db_column='customer', max_length=20)
    customer_phone = models.CharField(db_column='customer_phone', max_length=11)
    order_type = models.ForeignKey(information_models.Order_type, related_name='order', on_delete=models.CASCADE, db_column='order_type')
    pay_type = models.ForeignKey(information_models.Pay_type, related_name='order', on_delete=models.CASCADE, db_column='pay_type')
    pay_check = models.CharField(db_column='pay_check', max_length=1)

    class Meta:
        db_table = 'order'


class Order_item(models.Model):
    order_item_no = models.AutoField(db_column='order_item_id', primary_key=True)
    pk_no = models.ForeignKey(Order, related_name='order_item', on_delete=models.CASCADE, db_column='pk_no')
    product_id = models.ForeignKey(information_models.Product, related_name='order_item', on_delete=models.CASCADE, db_column='product_id')
    state = models.CharField(db_column='state', max_length=20)
    receipt_date = models.DateTimeField(db_column='receipt_date', )
    size_option = models.ForeignKey(information_models.Size, related_name='order_item', on_delete=models.CASCADE, db_column='size_id')
    sheet_option = models.ForeignKey(information_models.Sheet, related_name='order_item', on_delete=models.CASCADE, db_column='sheet_id')
    filling_option = models.ForeignKey(information_models.Filling, related_name='order_item', on_delete=models.CASCADE, db_column='filling_id')
    boxing_option = models.ForeignKey(information_models.Boxing, related_name='order_item', on_delete=models.CASCADE, db_column='boxing_id')
    phrase_option = models.CharField(db_column='phrase', max_length=1)
    count = models.IntegerField(db_column='count', )
    total_price = models.IntegerField(db_column='total_price', )
    recipient = models.CharField(db_column='recipient', max_length=20)
    recipient_phone = models.CharField(db_column='recipient_phone', max_length=11)
    delivery_option = models.ForeignKey(information_models.Delivery, related_name='order_item', on_delete=models.CASCADE, db_column='delivery_id')
    address = models.TextField(db_column='address', )
    memo = models.TextField(db_column='memo', )

    class Meta:
        db_table = 'order_item'
