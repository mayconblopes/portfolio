from django.db import models


class Iam(models.Model):
    hello_msg = models.CharField(max_length=100, verbose_name="Mensagem de boas vindas")
    name = models.CharField(max_length=5000, verbose_name="Meu nome")
    featured_skills = models.CharField(max_length=5000, verbose_name="Tags de competências [separe com vírgula]")
    address = models.CharField(max_length=750, verbose_name="Endereço profissional")
    telephone = models.CharField(max_length=750, verbose_name="Número de telefone")
    email = models.EmailField(verbose_name="E-mail")
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    whatsapp = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'I Am'

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo do 'Sobre'")
    simple_description = models.TextField(max_length=5000, verbose_name="Descrição suscinta sobre mim")
    more_description = models.TextField(max_length=5000, verbose_name="Descrição em mais detalhes sobre mim")

    class Meta:
        verbose_name_plural = 'Sobre'

    def __str__(self):
        return self.title


class Competence(models.Model):
    icon = models.CharField(max_length=200,
                            verbose_name="Icon class (ex: Font Awesome)")  # Icon is a Font Awesome icon https://fontawesome.com/
    name = models.CharField(max_length=25, verbose_name="Nome da competência")
    description = models.TextField(max_length=85, verbose_name="Descrição")
    index_order = models.IntegerField(verbose_name="Ordem de exibição", default=0)

    class Meta:
        verbose_name = 'Competência'
        ordering = ('index_order',)

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome do Cargo ou do Título Acadêmico")
    where = models.CharField(max_length=250, verbose_name="Local")
    when = models.CharField(max_length=50, verbose_name="Quando [Ano-Inicio - Ano-Fim]")
    description = models.TextField(max_length=85, verbose_name="Descrição do Cargo ou do Título Acadêmico")
    index_order = models.IntegerField(verbose_name="Ordem de exibição", default=0)

    class Meta:
        verbose_name = 'Experiência'
        ordering = ('index_order',)

    def __str__(self):
        return self.name


class Papper(models.Model):
    title = models.CharField(max_length=250, verbose_name="Título da obra/texto")
    abstract = models.TextField(max_length=250, verbose_name="Resumo")
    link = models.URLField(verbose_name="Link da obra /texto")
    index_order = models.IntegerField(verbose_name="Ordem de exibição", default=0)

    class Meta:
        verbose_name = 'Papper'
        ordering = ('index_order',)

    def __str__(self):
        return self.title


class Award(models.Model):
    who = models.CharField(max_length=50, verbose_name="Quem premiou/reconheceu")
    description = models.TextField(max_length=250, verbose_name="Descrição do prêmio")
    link = models.URLField(verbose_name="Link para prova da premiação/reconhecimento")
    index_order = models.IntegerField(verbose_name="Ordem de exibição", default=0)

    class Meta:
        verbose_name = 'Reconhecimento'
        ordering = ('index_order',)

    def __str__(self):
        return self.who + ": " + self.description[:65] + "(...)"


class PortfolioItem(models.Model):
    image_url = models.URLField(verbose_name="Link da imagem do produto")
    video_embed_code = models.TextField(verbose_name="Código HTML do video incorporado (embedded)", null=True, blank=True)
    name = models.CharField(max_length=18, verbose_name="Nome do produto")
    product_owner = models.CharField(max_length=200, verbose_name="Demandante")
    description = models.TextField(max_length=1000, verbose_name="Descrição do produto desenvolvido")
    github_link = models.URLField(verbose_name="Link do github", null=True, blank=True)
    website_link = models.URLField(verbose_name="Link do website", null=True, blank=True)
    index_order = models.IntegerField(verbose_name="Ordem de exibição", default=0)

