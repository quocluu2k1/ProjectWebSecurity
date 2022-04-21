from django.urls import reverse
from category.models import Category
from accounts.models import Account
from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=300, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)   
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

variation_category_choice = (
    ('variation', 'variation'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    objects = VariationManager()

    def __str__(self):
        return self.variation_value


class ReviewRating(models.Model):
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=1000, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=50, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    def __str__(self):
        return self.subject
