from django.db import models
from django.db.models import Q
from django.conf import settings
from django.db.models.signals import pre_save
from django.contrib.contenttypes.fields import GenericRelation

from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin, HitCount

from category.models import Category
from tags.models import Tag

User = settings.AUTH_USER_MODEL

from .utils import upload_image_path, generate_eight_digit_random_product_id
from jtro_ecommerce.utils import unique_slug_generator


class ProductQuerySet(models.QuerySet):
    pass


class ProductManager(models.Manager):
    pass


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.CharField(unique=True, blank=True, max_length=10)
    title = models.CharField(max_length=250)
    description = RichTextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to=upload_image_path)
    video = models.URLField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='product_tag')
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    quantity = models.IntegerField()
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        # ordering = ['-timestamp']
        verbose_name = 'Product Table'
        verbose_name_plural = 'Product Table'


def product_pre_order_id_save_receiver(sender, instance, *args, **kwargs):
    if not instance.product_id:
        instance.product_id = generate_eight_digit_random_product_id()


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
