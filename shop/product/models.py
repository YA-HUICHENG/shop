from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    pubDateTime = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)

    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pubDateTime']
        
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)
    pubDateTime = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.product.title + '-' + str(self.id)
    class Meta:
        ordering = ['pubDateTime']
        
class Cart(object):
    def __init__(self, *args, **kwargs):
        self.items = []
        self.total_price = 0
    def add_product(self,product):
        self.total_price += product.price
        for item in self.items:
            if item.product.id == product.id:
                item.quantity += 1
        return self.items.append(Product(product=product,unit_price=product.price,quantity=1))    
# Create your models here.
