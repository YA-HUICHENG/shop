from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    pubDateTime = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.PositiveIntegerField()
    
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
# Create your models here.
