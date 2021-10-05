from django.forms import ModelForm

from order_list.models import Order, Order_item


class SheetCreationOrder(ModelForm):
    class Meta:
        model = Order
        fields = ['order_type', 'customer', 'customer_phone', 'pay', 'pay_check']


class SheetCreationOrderItem(ModelForm):
    class Meta:
        model = Order_item
        fields = ['receipt_date', 'count', 'total_price', 'recipient', 'recipient_phone', 'address', 'memo']