from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Statonary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)


class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY)
    quantity = models.PositiveIntegerField(null=True)
    
    # class Meta:
    #     verbose_name_plural = 'Product' prevents the model class from being displayed in plural form
    
    def __str__(self):
        return f'{self.name} -- {self.quantity}'
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'
    
    
    
    
    