from django.db import models


class ProductServicesColorQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class ProductServicesManager(models.Manager):
    def get_queryset(self):
        return ProductServicesColorQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


class ProductServices(models.Model):
    service = models.CharField(max_length=25)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = ProductServicesManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Product Services'
        verbose_name_plural = 'Product Services'
