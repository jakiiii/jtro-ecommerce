# Generated by Django 2.2 on 2020-11-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_address', models.TextField(max_length=250)),
                ('phone', models.CharField(max_length=18)),
                ('email', models.EmailField(max_length=32)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Office Address',
                'verbose_name_plural': 'Office Address',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=32)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Message Table',
                'verbose_name_plural': 'Message Table',
                'ordering': ['-timestamp'],
            },
        ),
    ]
