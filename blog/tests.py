from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post
class BlogTestCase(TestCase):
    def setUp(self):
       self.client = Client()
       self.user = User.objects.create_user(
           username='testuser',
           password='testpass123'
)

       self.post = Post.objects.create(
        title='Test Post',
        content='Test content',
        author=self.user
)
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
    def test_health_check(self):
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'OK')