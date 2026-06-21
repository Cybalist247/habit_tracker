from datetime import datetime, timedelta
def list_all_habits(habits):
    """Returns all habits.
    Args:
        habits (list): List of habits.
    Returns:
        List: Complete habit list."""
    return habits

def habits_by_periodicity(habits, periodicity):
    """Filters habbits by periodicity.
    Args:
        habits (list): List of habits.
        periodicity (str): daily or weekly.
    Returns:
        List : Filtered habits.""" 

    return [habit for habit in habits if habit[2] == periodicity]

def count_habits(habits): 
    """Counts the total number of habits.
    Args:
        habits (list): List of habits.
    Returns:
        int: Total number of habits."""

    return len(habits)

def count_daily_habits(habits):
    """Counts all adily habits.
    Args:
        habits (list): List of habits
    Returns:
        int: Number of daily habits"""

    return len([habit for habit in habits if habit[2] == "daily"])  

def count_weekly_habits(habits):
    """Counts allweekly habits.
    Args:
        habits (list): List of habits.
    Returns:
        int: Number of weeklt habits."""

    return len([habit for habit in habits if habit[2] == "weekly"])  

def longest_streak(habits):
    """Returns the longest streak value.
    Args:
        habits (list): List of habits.
    Returns:
        int: Longest streak."""
        
    return max([1 for h in habits], default=0)              

def calculate_streak(completions):
    """Calculates the streak from completion dates"""
    if not completions:
        return 0

    dates = sorted(
        set(datetime.fromisoformat(c[0]).date() for c in completions)
    ) 
    current_streak = 1
    longest_streak = 1
    
    for i in range(1, len(dates)):
        if dates[i] - dates[i - 1] == timedelta(days=1):
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 1

    return longest_streak   
    