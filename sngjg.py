capacity = int(input("Enter bus capacity: "))
passengers = 0
for stop in range(1, 4):
    boarding = int(input("How many board? "))
    alighting = int(input("How many get off? "))
    passengers = passengers + boarding - alighting
    print("Passengers on bus:", passengers)
    if passengers > capacity:
        print("Capacity exceeded")

  
