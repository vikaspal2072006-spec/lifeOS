

print("================================")
print("       WELCOME TO LIFEOS")
print("================================")

print("Build better habits, build a better life.")

name = input("Enter your name: ")

print("\nHello", name + "!")
print("Let's start tracking your habits.")

# store daily habits

habits=[
    "Wake Up early",
    "Exercise",
    "Create Project",
    "Study python ",
    "Practice English",
    "Read books",
    "Drink enough water ",
]

#Display habits
print("\n=========== MY DAILY HABITS ===========")
for index, habit in enumerate(habits,start=1):
    print(index,habit)



print("\n======  ADD NEW HABIT ======")

new_habit=input("Add New Habit :- ")
habits.append(new_habit)

print("\n Updated Habit List")
for habit in habits:
    print("-",habit)

print("====== REMOVE A HABIT ======")

remove_habit=input("Enter Habit to remove :- ").strip().lower()
found = False
for habit in habits:
    if habit.strip().lower() == remove_habit.strip().lower():
        habits.remove(habit)
        found = True
        break
if found:
    print("Habit Remove Successfully!!")
else:
    print("habit not found")

for habit in habits:
    print("-",habit)

print("\n====== HABIT SUMMARY ======")
total_habit=len(habits)
print("TOTAL HABITS :- ",total_habit)

print("\n ======= CHECK HABIT ======")

check_habit=(input("ENTER HABIT TO CHECK :- ")).strip().lower()
if check_habit in [habit.lower() for habit in habits]:
    print("Habit exists!")
else:
    print("Habit does not exist")

print("\n====== SORTED HABITS =======")

habits.sort()
for habit in habits:
    print("-",habit)

habit_records = {
    "Exercise": {
        "2026-11-23": True,
        "2026-11-24": False
    },
    "Study Python": {
        "2026-11-23": True,
        "2026-11-24": False
    }
}
print(habit_records["Exercise"])
print(habit_records["Exercise"]["2026-11-23"])
print(habit_records["Study Python"]["2026-11-24"])
# Update Exercise status
habit_records["Exercise"]["2026-11-24"] = True

print("\nUpdated Exercise Records:")
print(habit_records["Exercise"])

complete_count = 0
pending_count = 0
for habit in habit_records:
    print("\nHabit",habit)

    for date in habit_records[habit]:
        if habit_records[habit][date]==True:
            print(date,": completed")
            complete_count += 1
        else:
            print(date,":pending")
            pending_count += 1

print("\nCompleted : ",complete_count)
print("\nPending : ", pending_count)

if total_habit >0:
    process=(complete_count/total_habit)*100
else:
    process=0

print("======DAILY PROCESS======")
print("Total Habits :- ",total_habit)
print("Completed :- ",complete_count)
print("Pending :- ",pending_count)
print("Completion percentage:",process,"%")
