import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django_app.django_api.serializers import CommentsSerializer
from django_app.models import Comments, Player


class TestApi(APITestCase):
    def setUp(self):
        self.player_1 = Player.objects.create(name='name_1', surname='surname_1', date_of_birth='1987-01-28')
        self.player_2 = Player.objects.create(name='name_2', surname='surname_2', date_of_birth='1987-02-20')
        self.comment_1 = Comments.objects.create(player=self.player_1, comment_text='comment text 1')
        self.comment_2 = Comments.objects.create(player=self.player_2, comment_text='comment text 2')
        self.comment_3 = Comments.objects.create(player=self.player_1, comment_text='comment text 3')

    def test_serializer(self):
        """ Тест сериализации данных """
        url = reverse('comments-list')
        response = self.client.get(url)
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many=True)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_filter(self):
        """ Тест фильтрации, получения комментариев по игроку команды """
        url = reverse('comments-list')
        response = self.client.get(url, data={'player': self.player_1.pk})
        comments = Comments.objects.filter(player=self.player_1.pk)
        serializer = CommentsSerializer(comments, many=True)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    def test_create(self):
        """ Тест создания объекта """
        url = reverse('comments-list')
        data = {"player": self.player_2.pk, "comment_text": "create comment"}
        data_json = json.dumps(data)

        response = self.client.post(url, data=data_json, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)  # Статус запроса post.
        self.assertEqual(4, Comments.objects.all().count())  # Количество комментариев после create.
