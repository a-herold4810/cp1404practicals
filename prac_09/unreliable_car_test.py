from unreliable_car import UnreliableCar

def main():
    # Create an UnreliableCar with 50% reliability
    unreliable_car = UnreliableCar("Test Car", 100, 50)

    # Attempt to drive 10 times and print results
    for i in range(1, 11):
        distance_to_drive = 20
        actual_distance = unreliable_car.drive(distance_to_drive)
        print(f"Attempt {i}: Tried to drive {distance_to_drive}km, actually drove {actual_distance}km")
        print(f"Fuel remaining: {unreliable_car.fuel}")

if __name__ == "__main__":
    main()