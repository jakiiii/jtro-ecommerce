from django.db import models

from jtro_ecommerce.utils import upload_image_path
from ckeditor.fields import RichTextField


class AboutWebProfile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_image_path)
    motto = models.CharField(max_length=250, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Web Profile"
        verbose_name_plural = "Web Profile"


class SocialMediaQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class SocialMediaManager(models.Manager):
    def get_queryset(self):
        return SocialMediaQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


class SocialMedia(models.Model):
    name = models.CharField(max_length=35, null=True, blank=True)
    link = models.URLField(max_length=150)
    icon = models.CharField(max_length=150, null=True, blank=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = SocialMediaManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Our Social Media"
        verbose_name_plural = "Our Social Media"


class FooterPaymentMethodStickerQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class FooterPaymentMethodStickerManager(models.Manager):
    def get_queryset(self):
        return FooterPaymentMethodStickerQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all()


class FooterPaymentMethodSticker(models.Model):
    name = models.CharField(max_length=35, null=True, blank=True)
    link = models.URLField(max_length=150)
    image = models.ImageField(upload_to=upload_image_path)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = FooterPaymentMethodStickerManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Our Payment Method"
        verbose_name_plural = "Our Payment Method"


class FAQ(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    text = RichTextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ"
