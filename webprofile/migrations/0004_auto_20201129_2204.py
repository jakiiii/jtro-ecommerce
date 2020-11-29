# Generated by Django 2.2 on 2020-11-29 22:04

from django.db import migrations, models
import jtro_ecommerce.utils


class Migration(migrations.Migration):

    dependencies = [
        ('webprofile', '0003_auto_20201129_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutWebProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=jtro_ecommerce.utils.upload_image_path)),
                ('motto', models.CharField(max_length=250)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Web Profile',
                'verbose_name_plural': 'Web Profile',
            },
        ),
        migrations.DeleteModel(
            name='FooterPaymentMethodStickerQuerySet',
        ),
        migrations.RemoveField(
            model_name='footerpaymentmethodsticker',
            name='icon',
        ),
        migrations.AddField(
            model_name='footerpaymentmethodsticker',
            name='image',
            field=models.ImageField(default=23.12, upload_to=jtro_ecommerce.utils.upload_image_path),
            preserve_default=False,
        ),
    ]