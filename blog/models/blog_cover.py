from django.db import models

from jtro_ecommerce.utils import upload_image_path


class BlogCover(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to=upload_image_path)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']
