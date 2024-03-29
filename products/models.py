"""
The models draw inspiration from:
- Boutique Ado project

Referenced websites:
- https://realpython.com/django-models-databases/

"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=254)
    web_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_for_web(self):
        return self.web_name


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, blank=False)
    description = models.TextField(blank=False)
    sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=True, blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(5)],)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    is_sales = models.BooleanField(default=False)
    sales_price = models.DecimalField(
        default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user_wishlist = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_wishlist')
    products = models.ManyToManyField(
        Product,
        related_name='wishlists',
        blank=True)

    def __str__(self):
        return f"Wishlist for {self.user_wishlist.username}"


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True, blank=False,
        validators=[MinValueValidator(0), MaxValueValidator(5)],)
    comment = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.name}"
