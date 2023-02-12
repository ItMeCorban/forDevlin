hour = int(input("What hour are you going? enter 24 hour number: "))
guard = input("Is the guard present? y/n: ")

if hour >= 7 and hour <= 17:
    print("Gate is open, you can enter")
else:
    if guard == "y":
        print("Guard is on duty, you can enter")
    else:
        print("Gate is locked, you can't enter")
