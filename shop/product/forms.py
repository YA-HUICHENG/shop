from django import forms
from product.models import Product
from product.models import Order
class ProductForm(forms.ModelForm):
    title = forms.CharField(label='產品名稱', max_length=128)
    content = forms.CharField(label='內容', widget=forms.Textarea)
    price = forms.CharField(label='價格', widget=forms.NumberInput())
    class Meta:
        model = Product
        fields = ['title', 'content','price']

class OrderForm(forms.ModelForm):
    Name = forms.CharField(label='姓名', max_length=128)
    adress = forms.CharField(label='地址', max_length=128)
    phone = forms.CharField(label='聯絡電話',max_length=12)
    number = forms.CharField(label='購買數量', widget=forms.NumberInput())

    class Meta:
        model = Order
        fields = ['Name', 'adress','phone','number']