# Generated by Django 4.1 on 2022-08-16 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_alter_portfolioitem_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='video_url',
            field=models.URLField(blank=True, null=True, verbose_name='Link do video do produto'),
        ),
    ]
