from django.forms import Form

from order_list.models import Order


class SheetCreationOrder(Form):
    class Meta:
        model = Order
        fields = ['order_type', 'customer', 'customer_phone', 'pay', 'pay_check']

