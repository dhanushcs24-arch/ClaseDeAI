def simple_reflex_agent(room_a, room_b, position):
    print("SIMPLE REFLEX AGENT")

    rooms = {
        "A": room_a,
        "B": room_b
    }

    while True:
        print("Vacuum is in Room", position)

        if rooms[position] == "D":
            print("SUCK")
            rooms[position] = "C"

        elif position == "A":
            print("MOVE RIGHT")
            position = "B"

        elif position == "B":
            print("MOVE LEFT")
            position = "A"

        if rooms["A"] == "C" and rooms["B"] == "C":
            print("Both rooms are clean.")
            print("STOP")
            break

print("VACUUM CLEANER AGENT")

room_a = input("Enter status of Room A (D/C): ").upper()
room_b = input("Enter status of Room B (D/C): ").upper()

while room_a not in ["D", "C"] or room_b not in ["D", "C"]:
    print("Enter only D for Dirty or C for Clean.")
    room_a = input("Enter status of Room A (D/C): ").upper()
    room_b = input("Enter status of Room B (D/C): ").upper()

position = input("Enter starting position (A/B): ").upper()

while position not in ["A", "B"]:
    position = input("Enter starting position (A/B): ").upper()

print("Initial State:")
print("Room A:", room_a)
print("Room B:", room_b)
print("Vacuum Position:", position)

simple_reflex_agent(room_a, room_b, position)