from django.test import TestCase
from django.urls import reverse
from slugify import slugify

from django_app.models import Comments, Player


class TestLogic(TestCase):
    def setUp(self):
        self.player_1 = Player.objects.create(name='name-1', surname='surname-1', date_of_birth='1987-01-28')
        self.player_2 = Player.objects.create(name='name-2', surname='surname-2', date_of_birth='1987-02-20')
        self.comment_1 = Comments.objects.create(player=self.player_1, comment_text='comment text 1')
        self.comment_2 = Comments.objects.create(player=self.player_2, comment_text='comment text 2')
        self.comment_3 = Comments.objects.create(player=self.player_1, comment_text='comment text 3')

    def test_model_save_with_create_slug(self):
        """ Тестирование создания slug, сохранение модели """
        player = Player.objects.create(name='name_3', surname='surname_3', date_of_birth='1987-01-28')
        slug = slugify(f'{player.name} {player.surname}')

        self.assertEquals(player.slug, slug)
        self.assertEquals(3, Player.objects.all().count())

    def test_model_get_absolute_url(self):
        """ Тестирование метода get_absolute_url, получение игрока команды по slug """
        player = Player.objects.get(id=1)
        slug = player.slug
        self.assertEquals(player.get_absolute_url(), f'/player/{slug}/')

    def test_view_url_exists_at_desired_location(self):
        """ Тестирование url и urlpatterns name """
        response = self.client.get('')
        response_urlpatterns_name = self.client.get(reverse('player_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_urlpatterns_name.status_code, 200)

        response = self.client.get(f'/player/{self.player_1.slug}/')
        response_urlpatterns_name = self.client.get(reverse('player_detail', kwargs={'slug': self.player_1.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_urlpatterns_name.status_code, 200)
