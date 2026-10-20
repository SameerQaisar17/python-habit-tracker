import json
import os

FILE_NAME = "habits.json"


def load_habits():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_habits(habits):
    with open(FILE_NAME, "w") as file:
        json.dump(habits, file, indent=4)


habits = load_habits()

print("===== HABIT TRACKER =====")

while True:
    print("\n1. Add Habit")
    print("2. View Habits")
    print("3. Mark Habit as Completed")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        habit_name = input("Enter the habit name: ").strip()

        if habit_name:
            habits.append({
                "name": habit_name,
                "completed": False
            })
            save_habits(habits)
            print(f"'{habit_name}' added successfully!")
        else:
            print("Habit name cannot be empty.")

    elif choice == "2":
        if not habits:
            print("You haven't added any habits yet.")
        else:
            print("\n===== YOUR HABITS =====")

            for number, habit in enumerate(habits, start=1):
                status = "Completed" if habit["completed"] else "Not completed"
                print(f"{number}. {habit['name']} - {status}")

    elif choice == "3":
        if not habits:
            print("No habits available to complete.")
        else:
            print("\n===== YOUR HABITS =====")

            for number, habit in enumerate(habits, start=1):
                print(f"{number}. {habit['name']}")

            try:
                number = int(input("Enter the habit number to complete: "))

                if 1 <= number <= len(habits):
                    habit = habits[number - 1]

                    if habit["completed"]:
                        print("This habit is already completed!")
                    else:
                        habit["completed"] = True
                        save_habits(habits)
                        print(f"'{habit['name']}' marked as completed!")
                else:
                    print("Invalid habit number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option! Please choose 1-4.")