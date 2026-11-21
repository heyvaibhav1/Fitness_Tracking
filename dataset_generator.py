import csv
import random
import os

def create_dataset(filename="fitness_data.csv"):
    if os.path.exists(filename):
        return

    headers = ["ID", "Name", "Age", "Workout", "Duration", "Calories", "HR", "Steps"]
    names = ["Aarav", "Diya", "Rohan", "Ananya", "Kabir", "Meera"]
    workouts = ["Running", "Cycling", "Yoga", "HIIT", "Swimming"]
    rows = []

    random.seed(42)
    for i in range(1, 56):
        mins = random.randint(20, 80)
        cal = round(mins * random.uniform(5, 12), 1)
        hr = random.randint(100, 170)
        rows.append([f"F{100+i}", random.choice(names), random.randint(20, 50),
                     random.choice(workouts), mins, cal, hr, mins * 100])

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)