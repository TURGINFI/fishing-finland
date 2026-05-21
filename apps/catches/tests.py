from django.test import TestCase
from django.utils import timezone

from .forms import CatchLogForm


class CatchLogFormTests(TestCase):
    def test_future_catch_date_is_invalid(self):
        form = CatchLogForm(data={
            'fish_name': 'Pike',
            'caught_at': (timezone.localdate() + timezone.timedelta(days=1)).isoformat(),
        })

        self.assertFalse(form.is_valid())
        self.assertIn('caught_at', form.errors)

    def test_negative_measurements_are_invalid(self):
        form = CatchLogForm(data={
            'fish_name': 'Perch',
            'caught_at': timezone.localdate().isoformat(),
            'weight_kg': '-1',
            'length_cm': '-10',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('weight_kg', form.errors)
        self.assertIn('length_cm', form.errors)
