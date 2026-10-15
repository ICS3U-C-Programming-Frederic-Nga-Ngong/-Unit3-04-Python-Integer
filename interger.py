#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 18 2008
# Checks if a number is positive, negative or just zero


def main():

    # Get number from the user
    number = float(input("Enter a number : "))

    # Checks if it is negative
    if number < 0:
        print("{} is a negative number".format(number))

        # Checks if it is just zero
    elif number == 0:
        print("it is just zero")

    # Checks it it is positive
    else:
        print("{} is a positive number".format(number))


if __name__ == "__main__":

    main()
