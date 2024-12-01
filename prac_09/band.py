class Band:
    """ Band class representing a musical band with multiple musicians """

    def __init__(self, name):
        """ Initialise a Band with a name and an empty list of musicians """

        self.name = name
        self.musicians = []

    def __str__(self):
        """ Return a string representation of the band, listing its musicians """

        return f"{self.name} ({', '.join(musician.name for musician in self.musicians)})"

    def add(self, musician):
        """ Add a musician to the band """

        self.musicians.append(musician)

    def play(self):
        """ Simulate the band playing, with each musician playing their instruments """

        output = []
        for musician in self.musicians:
            if musician.instruments:
                output.append(f"{musician.name} is playing: {', '.join(map(str, musician.instruments))}")
            else:
                output.append(f"{musician.name} needs an instrument!")
        return "\n".join(output)
