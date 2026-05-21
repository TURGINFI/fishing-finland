from django.test import TestCase
from django.utils import timezone

from .forms import FishingGoalForm


class FishingGoalFormTests(TestCase):
    def test_unrealistic_year_is_invalid(self):
        form = FishingGoalForm(data={
            'year': timezone.localdate().year + 5,
            'target_fish': 'Zander',
            'target_count': 10,
            'progress': 0,
        })

        self.assertFalse(form.is_valid())
        self.assertIn('year', form.errors)
