from django.forms import ModelForm, Form

from order_list.models import Order


class ListCreationOrderForm(Form):
    class Meta:
        model = Order
        fields = ['order_type', 'customer', 'customer_phone', 'pay', 'pay_check']

