from django.forms import Form

from order_list.models import Order, Order_item


class SheetCreationOrder(Form):
    class Meta:
        model = Order
        fields = ['order_type', 'customer', 'customer_phone', 'pay', 'pay_check']


class SheetCreationOrderItem(Form):
    class Meta:
        model = Order_item
        fields = ['receipt_date', 'count', 'total_price', 'recipient', 'recipient_phone', 'address', 'memo']