import unittest
from analytics import calculate_streak

from analytics import (
    count_habits,
    count_daily_habits,
    count_weekly_habits,
    habits_by_periodicity
)

class TestAnalytics(unittest.TestCase):
    """Tests analytics functions."""

    def setUp(self):
        self.habits = [
            (1, "Drink Water", "daily"),
            (2, "Exercise", "daily"),
            (3, "Meditate", "weekly")
        ]

    def test_count_habits(self):
        self.assertEqual(count_habits(self.habits), 3)   

    def test_count_daily_habits(self):
        self.assertEqual(count_daily_habits(self.habits), 2)

    def test_count_weekly_habits(self):
        self.assertEqual(count_weekly_habits(self.habits), 1)     

    def test_habits_by_periodicity(self):   
        daily = habits_by_periodicity(self.habits, "daily")

    def test_calculate_streak(self):
        completions = [
            ("2026-01-01",),
            ("2026-01-02",),
            ("2026-01-03",),
            ("2026-01-04",)
        ]
        self.assertEqual(
            calculate_streak(completions), 4
        )

if __name__ == "__main__":
    unittest.main()             