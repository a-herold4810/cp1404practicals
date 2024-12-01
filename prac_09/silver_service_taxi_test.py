from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

def main():
    # Create a SilverServiceTaxi with fanciness of 2
    luxury_taxi = SilverServiceTaxi("Hummer", 200, 2)

    # Drive 18 km
    luxury_taxi.drive(18)

    # Print the taxi's details and fare
    print(luxury_taxi)
    print(f"Fare: ${luxury_taxi.get_fare():.2f}")

    # Assert the fare is correct (18 km, fanciness 2, flagfall 4.50)
    expected_fare = 18 * (Taxi.price_per_km * 2) + SilverServiceTaxi.flagfall
    assert abs(luxury_taxi.get_fare() - expected_fare) < 0.01, "Fare calculation is incorrect!"

if __name__ == "__main__":
    main()