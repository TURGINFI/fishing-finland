from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import BlogPost


class BlogVisibilityTests(TestCase):
    def test_public_pages_only_show_approved_posts(self):
        user = User.objects.create_user(username='writer', password='strong-pass-123')
        approved = BlogPost.objects.create(
            author=user,
            title='Approved post',
            excerpt='Visible',
            content='Approved content',
            status=BlogPost.Status.APPROVED,
        )
        pending = BlogPost.objects.create(
            author=user,
            title='Pending post',
            excerpt='Hidden',
            content='Pending content',
            status=BlogPost.Status.PENDING,
        )

        list_response = self.client.get(reverse('public_blog_list'))
        self.assertContains(list_response, approved.title)
        self.assertNotContains(list_response, pending.title)

        detail_response = self.client.get(reverse('public_blog_detail', args=[pending.pk]))
        self.assertEqual(detail_response.status_code, 404)
