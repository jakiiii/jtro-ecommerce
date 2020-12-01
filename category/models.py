from django.db import models
from django.db.models.signals import pre_save


from .utils import upload_image_path
from jtro_ecommerce.utils import unique_slug_generator


class CategoryQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


class Category(models.Model):
    category_name = models.CharField(max_length=40)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    subcategory = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    objects = CategoryManager()

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Table of Category'
        verbose_name_plural = 'Table of Category'

    @property
    def title(self):
        return self.category_name


def category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(category_pre_save_receiver, sender=Category)
