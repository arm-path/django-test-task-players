from django.db import models
from django.urls import reverse
from slugify import slugify


class Player(models.Model):
    """ Модель игроков """
    name = models.CharField('Имя', max_length=35)
    slug = models.SlugField('url', max_length=150, unique=True, blank=True)
    surname = models.CharField('Фамилие', max_length=45)
    image = models.ImageField('Фотография', upload_to='players/', default="players/noavatar.png")
    date_of_birth = models.DateField('Дата рождения', auto_now_add=False, auto_now=False)
    description = models.TextField('Описание', blank=True, null=True)
    views = models.PositiveIntegerField('Количество просмотров', default=0)

    def __str__(self):
        return f'{self.name} {self.surname}'

    def save(self, *args, **kwargs):
        """ Определение slug при добавлении в БД """
        self.slug = slugify(f'{self.name} {self.surname}')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('player_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class Comments(models.Model):
    """  Модель комментарий """
    player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name='Статья игрока')
    comment_text = models.TextField('Текст коментария', max_length=255)
    publication_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return f'{self.player} {self.comment_text[:25]}'

    class Meta:
        verbose_name = 'Коментария'
        verbose_name_plural = 'Коментарии'
        ordering = ['-publication_date']
