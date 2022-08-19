from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=80, verbose_name='Nome')
    bio = models.TextField(max_length=250, verbose_name='Biografia resumida')
    email = models.EmailField(verbose_name='Email')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class BlogPost(models.Model):

    STARS_CHOICE = (
       ('✧', '✧'),
       ('✧✧', '✧✧'),
       ('✧✧✧', '✧✧✧'),
       ('✧✧✧✧', '✧✧✧✧'),
       ('✧✧✧✧✧', '✧✧✧✧✧'),
    )
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Autor')
    tags = models.CharField(max_length=100, verbose_name='Tags (separe por vírgulas e coloque a principal em primeiro)')
    is_draft = models.BooleanField(verbose_name='É rascunho?', default=True)
    title = models.CharField(max_length=100, verbose_name='Título do post')
    slug = models.SlugField()
    cover = models.URLField(verbose_name='URL da imagem da capa')
    content = models.TextField(max_length=5000, verbose_name='Conteúdo do post')
    pub_date = models.DateField(verbose_name='Data de publicação', blank=True, null=True)
    stars = models.CharField(max_length=5, verbose_name="Estrelas", choices=STARS_CHOICE)

    class Meta:
        ordering = ('-pub_date', 'title',)

    def __str__(self):
        return f'{self.author}: {self.title}'
