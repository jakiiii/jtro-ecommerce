from django.db import models


class ProductSizeQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class ProductSizeManager(models.Manager):
    def get_queryset(self):
        return ProductSizeQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


class ProductSize(models.Model):
    size = models.CharField(max_length=25)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = ProductSizeManager()

    def __str__(self):
        return self.size

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Product Size'
        verbose_name_plural = 'Product Size'
