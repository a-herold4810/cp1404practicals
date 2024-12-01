COLOUR_TO_HEX = {
    "Coral": "#ff7f50", "Crimson": "#dc143c", "DarkGreen": "#006400", "DarkMagenta": "#8b008b", "DeepPink": "#ff1493",
    "Gold": "#ffd700", "HotPink": "#ff69b4", "Indigo": "#4b0082", "Khaki": "#f0e68c", "Lavender": "#e6e6fa"}

colour_name = input("Enter color name: ").capitalize()
while colour_name != "":
    try:
        print(f"The hex code for {colour_name} is {COLOUR_TO_HEX[colour_name]}")
    except KeyError:
        print("Invalid color name")
    colour_name = input("Enter color name: ").capitalize()
