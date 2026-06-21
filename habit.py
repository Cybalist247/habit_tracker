from datetime import datetime

class Habit:
    """ Represents a user habit and its completion history"""

    def __init__(self, name, periodicity):

        """Initializes a new Habit object.
        Args: 
        name (str): The name of the habit 
        periodicity (str): Frequency of the habit.(daily or weekly)."""

        self.name = name
        self.periodicity = periodicity
        self.created_date = datetime.now()
        self.completion_dates = []

    def complete_task(self):
        """Marks the habit as completed by storing the completion date and time"""

        completion_time = datetime.now()
        self.completion_dates.append(completion_time)

def get_streak(self):
    """Returns the current completion streak.
    Returns:
       int: Number of completed entries."""

    return
    len(self.completion_dates)
    def __str__(self):
        """Returns a readable string representaion of the habit.
        Returns:
            str: Habit name and periodicity."""

        return f"{self.name}({self.periodicity})"
