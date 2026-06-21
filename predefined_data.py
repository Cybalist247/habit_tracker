# from habit import Habit
from database import add_habit, get_habits, add_completion

def load_predefined_habits():
    """Loads predefined haitsinto the database for testing and demonstration"""
    
    habits = [
        ("Drink Water", "daily"),
        ("Exercise", "daily"),
        ("Read Book", "daily"),
        ("Meditate", "weekly"),
        ("Clean Room", "weekly") 
    ]
    # 4 weeks of completion history
    
    for day in range(1, 29):
        date = f"2026-01-{day:02d}"

        add_completion(1, date)  # Drink water

    exercise_days = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10, 21, 22, 23, 24, 25, 26
    ]   

    for day in exercise_days:
        date = f"2026-01-{day:02d}" 
        add_completion(2, date)

    weekly_dates = [
        "2026-01-05", "2026-01-12", "2026-01-19", "2026-01-26"
    ]    

    for date in weekly_dates:
        add_completion(4, date) # Meditate
        add_completion(5, date) # Clean Room
    existing_habits = get_habits()
    existing_names = [habit[1] for habit in existing_habits]

    for name, periodicity in habits:
        if name not in existing_names:
            add_habit(name, periodicity, "2026-01-01")