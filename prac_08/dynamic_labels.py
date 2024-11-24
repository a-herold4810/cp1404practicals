"""
Dynamic Labels
Estimate: 45 minutes
Start Time: 1417
Actual: 58 minutes
Finish Time: 1516
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

# Load the KV file
Builder.load_file("dynamic_labels.kv")

class DynamicLabelsApp(App):
    def __init__(self):
        super(DynamicLabelsApp, self).__init__()
        # Define the data model (list of names)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]

    def build(self):
        # Load the root widget (BoxLayout) from the KV file
        root = Builder.load_file("dynamic_labels.kv")  # Explicitly load from the KV file

        # Access the BoxLayout with the `id` defined in the KV file
        main_layout = root.ids.main

        # Dynamically create Label widgets and add them to the layout
        for name in self.names:
            label = Label(text=name)
            main_layout.add_widget(label)

        return root

if __name__ == "__main__":
    DynamicLabelsApp().run()