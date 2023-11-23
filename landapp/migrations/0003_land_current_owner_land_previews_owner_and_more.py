# Generated by Django 4.2.7 on 2023-11-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landapp', '0002_land_is_slider_alter_land_name_alter_land_name_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='Current_owner',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='land',
            name='previews_owner',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='land',
            name='image_5',
            field=models.ImageField(blank=True, upload_to='land/', verbose_name='Slider Image'),
        ),
    ]
