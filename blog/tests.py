from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):
    print("*" * 60)

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="secret"
        )

        self.post = Post.objects.create(
            title="Test Title",
            body="Boooooooddddddyyyy",
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title="Test Title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "Test Title")
        self.assertEqual(f"{self.post.author}", "testuser")
        self.assertEqual(f"{self.post.body}", "Boooooooddddddyyyy")

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Boooooooddddddyyyy")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detail_view(self):
        response = self.client.get("/post/1")
        no_response = self.client.get("/post/10000")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Test Title")
        self.assertTemplateUsed(response, "one_post.html")

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1')

    def test_post_create_view(self):
        response = self.client.post(reverse('new_post'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'New title')
        self.assertEqual(Post.objects.last().body, 'New text')

    def test_post_update_view(self):
        response = self.client.post(reverse('edit_post', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text'
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(
            reverse('delete_post', args='1')
        )
        self.assertEqual(response.status_code, 302)
