from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A more luxurious Taxi that includes a flagfall charge and fanciness multiplier"""

    flagfall = 4.50  # Class variable for the additional charge per trip

    def __init__(self, name, fuel, fanciness):
        """ Initialise a SilverServiceTaxi instance """

        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """ Calculate the fare for the trip, including the flagfall """

        return super().get_fare() + self.flagfall

    def __str__(self):
        """ Return a string representation of the SilverServiceTaxi, including the flagfall """

        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"