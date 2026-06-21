import unittest
from habit import Habit

class TestHabit(unittest.TestCase):
    """Tests the habit class functionality."""
    def test_habit_creation(self):
        """Tests whether a habit is created created properly."""

        habit = Habit("Exercise", "daily")
        self.assertEqual(habit.name, "Exercise")
        self.assertEqual(habit.periodicity, "daily")

    def test_complete_task(self):
        """Tests whether habit completion works correctly."""
        habit = Habit("Read", "daily")
        habit.complete_task()

        self.assertEqual(len(habit.completion_dates), 1)
 
if __name__ == "__main__":
    unittest.main()    