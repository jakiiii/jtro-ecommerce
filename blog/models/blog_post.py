from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import pre_save
from django.contrib.humanize.templatetags import humanize
from django.contrib.contenttypes.fields import GenericRelation

from ckeditor_uploader.fields import RichTextUploadingField
from hitcount.models import HitCountMixin, HitCount

from blog.utils import upload_image_path
from jtro_ecommerce.utils import unique_slug_generator

from blog.models.blog_category import BlogCategory

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)

    def category_name(self, category_slug):
        return BlogPost.objects.filter(category_name__blog_category_name__iexact=category_slug)

    def search(self, query):
        lookup = (
                Q(title__icontains=query) | Q(title__iexact=query) |
                Q(content__icontains=query) | Q(content__iexact=query) |
                Q(category_name__blog_category_name__icontains=query) |
                Q(category_name__blog_category_name__iexact=query)
        )
        return self.filter(lookup).distinct()


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def category_name(self, category_slug):
        return self.get_queryset().category_name(category_slug)

    def search(self, query):
        return self.get_queryset().search(query)


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

    def get_timestamp(self):
        return humanize.naturaltime(self.timestamp)

    def get_absolute_url(self):
        return reverse("blog-post-detail", kwargs={"slug": self.slug})


def blog_post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(blog_post_pre_save_receiver, sender=BlogPost)
