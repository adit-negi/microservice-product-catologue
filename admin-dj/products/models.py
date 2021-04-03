from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.FileField(blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'product'

    def __str__(self):
        if self.title:
            return self.title[:10]
        return None


class User(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'
