from django.db import models
from django.db.models import Q
from django.conf import settings
from django.db.models.signals import pre_save
from django.contrib.contenttypes.fields import GenericRelation

from ckeditor_uploader.fields import RichTextUploadingField
from hitcount.models import HitCountMixin, HitCount

from blog.utils import upload_image_path
from jtro_ecommerce.utils import unique_slug_generator

from blog.models.blog_category import BlogCategory

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    pass


class BlogPostManager(models.Manager):
    pass


class BlogPost(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    content = RichTextUploadingField()
    category_name = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blog_category')
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    objects = BlogPostManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Blog Post Table"
        verbose_name_plural = "Blog Post Table"


def blog_post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(blog_post_pre_save_receiver, sender=BlogPost)
