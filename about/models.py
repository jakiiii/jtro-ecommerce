from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from jtro_ecommerce.utils import upload_image_path


class About(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    description = RichTextUploadingField()
    timestamp = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return "ABOUT US"
