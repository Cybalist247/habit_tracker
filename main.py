#from database import get_completions
#from database import get_habit_completions
from analytics import calculate_streak
from database import get_habit_completions

from database import (
    create_tables,
    add_habit,
    get_habits,
    delete_habit,
    complete_habit
)

from analytics import (
    count_habits,
    count_daily_habits,
    count_weekly_habits
)
from predefined_data import load_predefined_habits

create_tables()

while True:
    print("\n--- Habit Tracker ---")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Load Predefined Habits")
    print("4. Delete Habit")
    print("5. Complete Habit")
    print("6. Analytics")
    print("7. Exit")

    choice = input("Choose an option: ")
     
    if choice == "1":
        name = input("Habit name: ")
        periodicity = input("daily or weekly: ")
        add_habit(name, periodicity, "2026-01-01")
        print("Habit added successfully!")

    elif choice == "2":
        habits = get_habits()
        if len(habits) == 0:
            print("No habits found.")

        else:
            for habit in habits:
                print(habit)    

    elif choice == "3":
        load_predefined_habits()
        print("Predefined habits loaded!")

    elif choice == "4":
        habit_id = input("Enter habit ID to delete: ")  

        delete_habit(habit_id)

        print("Habit deleted successfully!")  

    elif choice == "5":
        habit_id = input("Enter habit ID to complete: ")
        complete_habit(habit_id)
        print("Habit completed successfully!")    

    elif choice == "6":
        habits = get_habits()

        total = count_habits(habits)
        daily = count_daily_habits(habits)
        weekly = count_weekly_habits(habits)

        completions = get_habit_completions(1)
        streak = calculate_streak(completions)

        print("\n--- Habit Analytics ---") 
        print(f"Total habits tracked: {total}")
        print(f"Daily habits tracked: {daily}")  
        print(f"Weekly habits tracked: {weekly}") 
        print(f"Longest streak: {streak}")



    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
