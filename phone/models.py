from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class PhoneBrand(models.Model):
    name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.nationality}"

    class Meta:
        unique_together = ("name", "nationality")
        ordering = ['name']


class PhoneModel(models.Model):
    brand = models.ForeignKey(PhoneBrand, on_delete=models.CASCADE,
                              related_name='phone_model')
    model = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand.name} - {self.model} - {self.brand.nationality}"

    class Meta:
        unique_together = ("brand", "model")
        ordering = ['model']


class Phone(models.Model):
    phone_name = models.ForeignKey(PhoneModel, on_delete=models.CASCADE, related_name='phone')
    price = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10000)],
        help_text="The currency is the dollar"
    )
    color = models.CharField(max_length=100)
    screen_size = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(20.0)],
        help_text="Screen size in inches"
    )
    is_available = models.BooleanField(default=False)
    manufacturing_country = models.CharField(max_length=100)

    def __str__(self):
        return self.phone_name.model

    class Meta:
        unique_together = (
            'phone_name', 'price', 'color', 'screen_size', 'manufacturing_country'
        )
        ordering = ['-price']
