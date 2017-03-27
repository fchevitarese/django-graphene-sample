from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)
    picture = models.URLField(default='https://placehold.it/350x150')
    category = models.ForeignKey('Category', related_name='product_category')

    def __str__(self):
        return self.product

    def __unicode__(self):
        return self.product


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

