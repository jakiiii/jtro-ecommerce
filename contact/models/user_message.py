from django.db import models


class UserMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=32)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Message Table'
        verbose_name_plural = 'Message Table'
