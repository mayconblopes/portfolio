# Generated by Django 4.1 on 2022-08-19 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='likes',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='stars',
            field=models.CharField(choices=[('1', '✧'), ('2', '✧✧'), ('3', '✧✧✧'), ('4', '✧✧✧✧'), ('5', '✧✧✧✧✧')], default=5, max_length=5, verbose_name='Estrelas'),
            preserve_default=False,
        ),
    ]
