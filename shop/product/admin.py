from django.contrib import admin
from product.models import Product, Comment
from .models import Category, Product

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'content']
    list_display_links = ['product']
    list_filter = ['product', 'content']
    search_fields = ['content']
    list_editable = ['content']
    class Meta:
        model = Comment
        
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


admin.site.register(Product)
admin.site.register(Comment, CommentModelAdmin)


# Register your models here.
