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
        
class Order(models.Model):
    Name = models.CharField(max_length=128)
    adress = models.CharField(max_length=128)
    phone = models.CharField(max_length=12)
    number= models.IntegerField()



    def __str__(self):
        return self.Name
# Create your models here.
