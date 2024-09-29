""" 1. Write code that asks the user for their name, then opens a file called name.txt and writes that name to it.
    Use open and close for this question. """

out_file = open("name.txt", "w")
name = input("Enter your name: ")
out_file.write(name)
out_file.close()
