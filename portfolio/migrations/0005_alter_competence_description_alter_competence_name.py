# Generated by Django 4.1 on 2022-08-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_competence_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competence',
            name='description',
            field=models.TextField(max_length=85, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='competence',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Nome da competência'),
        ),
    ]
