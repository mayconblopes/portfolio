# Generated by Django 4.1 on 2022-08-18 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name="Titulo do 'Sobre'")),
                ('simple_description', models.TextField(max_length=5000, verbose_name='Descrição suscinta sobre mim')),
                ('more_description', models.TextField(max_length=5000, verbose_name='Descrição em mais detalhes sobre mim')),
            ],
            options={
                'verbose_name_plural': 'Sobre',
            },
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.CharField(max_length=50, verbose_name='Quem premiou/reconheceu')),
                ('description', models.TextField(max_length=250, verbose_name='Descrição do prêmio')),
                ('link', models.URLField(verbose_name='Link para prova da premiação/reconhecimento')),
                ('index_order', models.IntegerField(default=0, verbose_name='Ordem de exibição')),
            ],
            options={
                'verbose_name': 'Reconhecimento',
                'ordering': ('index_order',),
            },
        ),
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=200, verbose_name='Icon class (ex: Font Awesome)')),
                ('name', models.CharField(max_length=25, verbose_name='Nome da competência')),
                ('description', models.TextField(max_length=85, verbose_name='Descrição')),
                ('index_order', models.IntegerField(default=0, verbose_name='Ordem de exibição')),
            ],
            options={
                'verbose_name': 'Competência',
                'ordering': ('index_order',),
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome do Cargo ou do Título Acadêmico')),
                ('where', models.CharField(max_length=250, verbose_name='Local')),
                ('when', models.CharField(max_length=50, verbose_name='Quando [Ano-Inicio - Ano-Fim]')),
                ('description', models.TextField(max_length=85, verbose_name='Descrição do Cargo ou do Título Acadêmico')),
                ('index_order', models.IntegerField(default=0, verbose_name='Ordem de exibição')),
            ],
            options={
                'verbose_name': 'Experiência',
                'ordering': ('index_order',),
            },
        ),
        migrations.CreateModel(
            name='Iam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hello_msg', models.CharField(max_length=100, verbose_name='Mensagem de boas vindas')),
                ('name', models.CharField(max_length=5000, verbose_name='Meu nome')),
                ('featured_skills', models.CharField(max_length=5000, verbose_name='Tags de competências [separe com vírgula]')),
                ('address', models.CharField(max_length=750, verbose_name='Endereço profissional')),
                ('telephone', models.CharField(max_length=750, verbose_name='Número de telefone')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('whatsapp', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'I Am',
            },
        ),
        migrations.CreateModel(
            name='Papper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Título da obra/texto')),
                ('abstract', models.TextField(max_length=250, verbose_name='Resumo')),
                ('link', models.URLField(verbose_name='Link da obra /texto')),
                ('index_order', models.IntegerField(default=0, verbose_name='Ordem de exibição')),
            ],
            options={
                'verbose_name': 'Papper',
                'ordering': ('index_order',),
            },
        ),
        migrations.CreateModel(
            name='PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(verbose_name='Link da imagem do produto')),
                ('video_embed_code', models.TextField(blank=True, null=True, verbose_name='Código HTML do video incorporado (embedded)')),
                ('name', models.CharField(max_length=18, verbose_name='Nome do produto')),
                ('product_owner', models.CharField(max_length=200, verbose_name='Demandante')),
                ('description', models.TextField(max_length=1000, verbose_name='Descrição do produto desenvolvido')),
                ('github_link', models.URLField(blank=True, null=True, verbose_name='Link do github')),
                ('website_link', models.URLField(blank=True, null=True, verbose_name='Link do website')),
                ('index_order', models.IntegerField(default=0, verbose_name='Ordem de exibição')),
            ],
        ),
    ]
