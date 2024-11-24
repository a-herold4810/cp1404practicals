from car import Car
import random


class UnreliableCar(Car):
    """A car that has a reliability factor affecting its ability to drive."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """ Drive the car a given distance based on its reliability """
        if random.uniform(0, 100) < self.reliability:
            # Drive the car as usual if it "succeeds" reliability check
            return super().drive(distance)
        else:
            # The car fails to drive any distance
            return 0