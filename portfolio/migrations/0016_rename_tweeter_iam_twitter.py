# Generated by Django 4.1 on 2022-08-17 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_iam_address_iam_email_iam_github_iam_instagram_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iam',
            old_name='tweeter',
            new_name='twitter',
        ),
    ]
