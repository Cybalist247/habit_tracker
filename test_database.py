import unittest
from database import create_tables, add_habit, get_habits

class TestDatabase(unittest.TestCase):

    def test_add_habit(self):
        create_tables()

        add_habit(
            "Test Habit",
            "daily",
            "206-01-01"
        )
        habits = get_habits()

        self.assertTrue(
            any(habit[1] == "Test Habit" for habit in habits)
        )


    def test_delete_habit(self):
        from database import delete_habit

        add_habit(
               "Delete Me",
               "daily",
               "2026-01-01"
             )   

        habits = get_habits()
        habit_id = habits[-1][0]
        delete_habit(habit_id) 
        habits_after = get_habits()

        self.assertFalse(
            any(h[0] == habit_id for h in habits_after)
        )

if __name__ == "__main__":
    unittest.main()        

