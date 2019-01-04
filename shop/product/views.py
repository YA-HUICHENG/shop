from django.shortcuts import render

def product(request):
    '''
    Render the product page
    '''
    return render(request, 'product/product.html')
# Create your views here.
