from django import forms
from product.models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='產品名稱', max_length=128)
    content = forms.CharField(label='內容', widget=forms.Textarea)
    price = forms.CharField(label='價格', widget=forms.NumberInput())
    class Meta:
        model = Product
        fields = ['title', 'content','price']