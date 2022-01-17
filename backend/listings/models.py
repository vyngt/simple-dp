from django.db import models
from django.contrib.auth.models import User


class Listings(models.Model):
    class SaleType(models.TextChoices):
        PICK_UP = "Available for pickup"
        SHIP = "Available for shipping"

    class ConditionType(models.TextChoices):
        USED = "Used"
        NEW = "New"

    class ProductType(models.TextChoices):
        BIKE = "Bike"
        PARTS = "Parts"
        MODELS = "Models"
        OTHER = "Other"

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    condition = models.CharField(
        max_length=50, choices=ConditionType.choices, default=ConditionType.USED
    )
    product_type = models.CharField(
        max_length=50, choices=ProductType.choices, default=ProductType.BIKE
    )
    sale_type = models.CharField(
        max_length=50, choices=SaleType.choices, default=SaleType.SHIP
    )
    price = models.FloatField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zipcode = models.CharField(max_length=25)
    main_photo = models.ImageField()
    photo_1 = models.ImageField()
    photo_2 = models.ImageField(blank=True)
    list_date = models.DateTimeField(auto_now_add=True)
    contact_email = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Listings"