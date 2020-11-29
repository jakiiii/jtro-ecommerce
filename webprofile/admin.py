from django.contrib import admin

from .models import (
    AboutWebProfile,
    SocialMedia,
    FooterPaymentMethodSticker,
    FAQ
)


@admin.register(AboutWebProfile)
class AboutWebProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'timestamp']


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'timestamp']


@admin.register(FooterPaymentMethodSticker)
class FooterPaymentMethodStickerAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'timestamp']


admin.site.register(FAQ)
