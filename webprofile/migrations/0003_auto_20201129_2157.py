# Generated by Django 2.2 on 2020-11-29 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webprofile', '0002_auto_20201129_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterPaymentMethodSticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=35, null=True)),
                ('link', models.URLField(max_length=150)),
                ('icon', models.CharField(blank=True, max_length=150, null=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Our Payment Method',
                'verbose_name_plural': 'Our Payment Method',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='FooterPaymentMethodStickerQuerySet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='socialmedia',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Our Social Media', 'verbose_name_plural': 'Our Social Media'},
        ),
    ]