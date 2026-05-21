from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Event, EventRegistration


class EventRegistrationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='angler', password='strong-pass-123')
        self.event = Event.objects.create(
            title='Lake meetup',
            description='Morning fishing session',
            location='Tampere',
            start_time=timezone.now() + timezone.timedelta(days=2),
            end_time=timezone.now() + timezone.timedelta(days=2, hours=3),
            max_participants=1,
        )

    def test_registration_requires_post(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('register_for_event', args=[self.event.pk]))

        self.assertEqual(response.status_code, 405)
        self.assertFalse(EventRegistration.objects.exists())

    def test_full_event_blocks_new_registration(self):
        first_user = User.objects.create_user(username='first', password='strong-pass-123')
        EventRegistration.objects.create(user=first_user, event=self.event)
        self.client.force_login(self.user)

        response = self.client.post(reverse('register_for_event', args=[self.event.pk]))

        self.assertRedirects(response, reverse('event_detail', args=[self.event.pk]))
        self.assertFalse(EventRegistration.objects.filter(user=self.user, event=self.event).exists())

    def test_event_end_time_must_be_after_start_time(self):
        event = Event(
            title='Bad event',
            description='Invalid times',
            location='Helsinki',
            start_time=timezone.now(),
            end_time=timezone.now() - timezone.timedelta(hours=1),
        )

        with self.assertRaisesMessage(Exception, 'End time must be after start time.'):
            event.full_clean()
