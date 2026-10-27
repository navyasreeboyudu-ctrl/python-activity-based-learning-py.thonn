
prepared = int(input("Meals prepared: "))
served = int(input("Meals served: "))
leftovers = prepared - served
print("Leftover meals:", leftovers)
if leftovers > 2:
    print("Too much food was wasted.")
else:
    print("Food waste is acceptable.")
