"""
Miles to Kilometres Convertor
Estimate: 30 minutes
Start Time: 1327
Actual: 39 minutes
Finish Time: 1406
"""

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Constant for conversion factor
MILES_TO_KM = 1.60934


class MilesToKmConverterApp(App):
    # StringProperty for dynamic updates to the output label
    km_output = StringProperty("0.0")

    def build(self):
        """ Build the Kivy app """

        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_conversion(self):
        """ Convert miles to kilometers and update the output label """

        try:
            miles = float(self.root.ids.input_miles.text)
            kilometers = miles * MILES_TO_KM
            self.km_output = f"{kilometers:.2f}"
        except ValueError:
            # Set output to 0.0 if the input is invalid
            self.km_output = "0.0"

    def handle_increment(self, change):
        """ Increment or decrement the miles value """

        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0  # Default to 0 if input is invalid
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_conversion()


if __name__ == "__main__":
    MilesToKmConverterApp().run()