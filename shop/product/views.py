from django.shortcuts import render

from product.models import Product, Comment

def product(request):
    '''
    Render the product page
    '''
    products = {}
    for product in Product.objects.all():
        products.update({product:Comment.objects.filter(product=product)})
    context = {'products':products}
    return render(request, 'product/product.html', context)
# Create your views here.
