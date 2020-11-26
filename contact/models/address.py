from django.db import models


class Address(models.Model):
    office_address = models.TextField(max_length=250)
    phone = models.CharField(max_length=18)
    email = models.EmailField(max_length=32)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return self.office_address

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Office Address"
        verbose_name_plural = "Office Address"
