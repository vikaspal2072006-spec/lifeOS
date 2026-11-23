

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
print("=========== MY DAILY HABITS ===========")
for habit in habits:
    print("-",habit)

print("\n===== HABIT DETAILS ======")
print("1",habits[0])
print("2",habits[1])
print("3",habits[2])
print("4",habits[3])
print("5",habits[4])
print("6",habits[5])
print("7",habits[6])

print("======  ADD NEW HABIT ======")

new_habit=input("Add New Habit :- ")
habits.append(new_habit)

print("\n Updated Habit List")
for habit in habits:
    print("-",habit)

print("====== REMOVE A HABIT ======")

remove_habit=(input("Enter Habit to remove :- ".strip().lower()))
found = False
for habit in habits:
    print("Checking:", repr(habit), "vs", repr(remove_habit))
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
