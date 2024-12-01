
numbers = [3, 1, 4, 1, 5, 9, 2]

""" 1. numbers[0]
    2. numbers[-1]
    3. numbers[3]
    4. numbers[:-1]
    5. numbers[3:4]
    6. 5 in numbers
    7. 7 in numbers
    8. "3" in numbers
    9. numbers + [6, 5, 3] """

# 1. 3
# 2. 2
# 3. 1
# 4. [3, 1, 4, 1, 5, 9]
# 5. [1]
# 6. True
# 7. False
# 8. False
# 9. [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

""" 1. Change the first element of numbers to "ten" (the string, not the number 10)
    2. Change the last element of numbers to 1
    3. Print all the elements from numbers except the first two (slice)
    4. Print whether 9 is an element of numbers """

# 1.
numbers[0] = "ten"

# 2.
numbers[-1] = 1

# 3.
print(numbers[2:])

# 4.
print(9 in numbers)
