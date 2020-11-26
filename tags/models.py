from django.db import models
from django.db.models.signals import pre_save

from jtro_ecommerce.utils import unique_slug_generator


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.tag_name

    @property
    def title(self):
        return self.tag_name

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Table of Tag Name'
        verbose_name_plural = 'Table of Tag Name'


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
