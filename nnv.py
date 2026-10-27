days = int(input("Enter number of days (28, 29, 30, or 31): "))
start = int(input("Enter starting weekday (Monday=0 to Sunday=6): "))
print("Mon Tue Wed Thu Fri Sat Sun")
# Print spaces before the first day
for i in range(start):
    print("    ", end="")
# Print the days
for day in range(1, days + 1):
    print(day, end="  ")
    if (start + day) % 7 == 0:
        print()

