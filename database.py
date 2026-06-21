import sqlite3
from datetime import datetime

def create_tables():
    """Creates the database tables if they do not exist."""

    conn = sqlite3.connect("habits.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS habits (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, periodicity Text, created_date TEXT)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS completions (id INTEGER PRIMARY KEY AUTOINCREMENT, habit_id INTEGER, completion_date TEXT)""")

    conn.commit()
    conn.close()

def add_habit(name, periodicity, ccreated_date):
    """Inserts a new habit into the database.
    Args:
        name (str): Habit name.
        periodicity (str): Habit frequency.
        created_date (str): Date created"""

    conn = sqlite3.connect("habits.db")
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO habits (name, periodicity, created_date)VALUES (?, ?, ?)""", (name, periodicity, str(ccreated_date)))

    conn.commit()
    conn.close()

def get_habits():
    """Retrieves all habits from the database.
       Returns:
           List: List of stored habits."""

    conn = sqlite3.connect("habits.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM habits")
    habits = cursor.fetchall() 

    conn.close()
    return habits   

def delete_habit(habit_id):
    """Deletes a habit from the database.
    Args:
        habit_id (int): ID of the habit to delete."""
        
    conn = sqlite3.connect("habits.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
    conn.commit()
    conn.close    

def complete_habit(habit_id):
    """Stores a completion record for a hbait.
    Args:
        habit_id (int): ID of completed habit."""
        
    conn = sqlite3.connect("habits.db")
    cursor = conn.cursor()

    completion_date = datetime.now()

    cursor.execute("""INSERT INTO completions (habit_id, completion_date) VALUES (?, ?)""", (habit_id, str(completion_date)))

    conn.commit()
    conn.close()
        
def add_completion(habit_id, completion_date):
    conn = sqlite3.connect("habits.db")
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO completions (habit_id, completion_date) VALUES (?, ?)""", (habit_id, completion_date))
    
    conn.commit()
    conn.close()

def get_completions():

    conn = sqlite3.connect("habits.db")    
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM completions")
    completions = cursor.fetchall()

    conn.close()
    return completions

def get_habit_completions(habit_id):
    """Returns all completion dates for a habit."""

    conn = sqlite3.connect("habits.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT completion_date FROM completions WHERE habit_id = ?", (habit_id, )
    )
    completions = cursor.fetchall()
    conn.close()
    return completions