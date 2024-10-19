"""
Word Occurrences
Estimate: 30 minutes
Actual:
"""

def main():
    emails = []

    while True:
        email = input("Email: ")
        if email == "":
            break
        emails.append(email)

    print("Emails collected:")
    for email in emails:
        print(email)


main()
