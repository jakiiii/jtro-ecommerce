from django.db import models


class ProductColorQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class ProductColorManager(models.Manager):
    def get_queryset(self):
        return ProductColorQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


class ProductColor(models.Model):
    color = models.CharField(max_length=25)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = ProductColorManager()

    def __str__(self):
        return self.color

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Product Color'
        verbose_name_plural = 'Product Color'
