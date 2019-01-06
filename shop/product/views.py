from django.shortcuts import render

from product.models import Product

def product(request):
    '''
    Render the product page
    '''
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'product/product.html', context)
# Create your views here.
