from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import PlatformMessage


class InboxTests(TestCase):
    def test_mark_message_read_requires_post_and_owner(self):
        user = User.objects.create_user(username='angler', password='strong-pass-123')
        other = User.objects.create_user(username='other', password='strong-pass-123')
        msg = PlatformMessage.objects.create(recipient=user, subject='Permit', body='Remember your permit.')
        other_msg = PlatformMessage.objects.create(recipient=other, subject='Private', body='Hidden.')
        self.client.force_login(user)

        get_response = self.client.get(reverse('mark_message_read', args=[msg.pk]))
        self.assertEqual(get_response.status_code, 405)
        msg.refresh_from_db()
        self.assertFalse(msg.is_read)

        owner_response = self.client.post(reverse('mark_message_read', args=[other_msg.pk]))
        self.assertEqual(owner_response.status_code, 404)

        post_response = self.client.post(reverse('mark_message_read', args=[msg.pk]))
        self.assertRedirects(post_response, reverse('inbox_list'))
        msg.refresh_from_db()
        self.assertTrue(msg.is_read)
