"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects_data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects_data.append(parts)

    input_file.close()
    return subjects_data


def print_subject_details(subjects):
    """ Displays subject data in a useful format """
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students.")

main()