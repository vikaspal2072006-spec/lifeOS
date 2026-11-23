

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