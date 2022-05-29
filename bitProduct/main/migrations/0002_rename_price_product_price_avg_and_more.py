# Generated by Django 4.0 on 2022-05-29 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='price_avg',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='stock',
            new_name='sallers',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='name_long_shop',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='name_short_shop',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
