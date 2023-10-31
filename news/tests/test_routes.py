# news/tests/test_routes.py
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class TestRoutes(TestCase):

    def test_home_page(self):
        # Вызываем метод get для клиента (self.client)
        # и загружаем главную страницу.
        url = reverse('news:home')
        response = self.client.get(url)
        # Проверяем, что код ответа равен 200.
        self.assertEqual(response.status_code, HTTPStatus.OK)