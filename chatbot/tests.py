import json
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class ChatbotTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_home_accessible(self):
        response = self.client.get(reverse('chatbot:home'))
        self.assertEqual(response.status_code, 200)

    def test_login_redirects_to_chat(self):
        response = self.client.post(reverse('chatbot:login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertRedirects(response, reverse('chatbot:home'))

    def test_register_creates_user(self):
        response = self.client.post(reverse('chatbot:register'), {
            'username': 'newuser',
            'password': 'newpass123'
        })
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_bot_returns_response(self):
        url = reverse('chatbot:get_chat_response')
        data = {'message': 'Hello bot!'}
        response = self.client.post(url, json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertIn('response', json_response)
        self.assertTrue(json_response['response'])
