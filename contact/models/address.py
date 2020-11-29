from django.db import models


class AddressQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class AddressManager(models.Manager):
    def get_queryset(self):
        return AddressQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


class Address(models.Model):
    office_address = models.TextField(max_length=250, null=True, blank=True)
    phone = models.CharField(max_length=18, null=True, blank=True)
    email = models.EmailField(max_length=32, null=True, blank=True)
    active = models.BooleanField(default=True)
    map_location = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    objects = AddressManager()

    def __str__(self):
        return self.office_address

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Office Address"
        verbose_name_plural = "Office Address"
