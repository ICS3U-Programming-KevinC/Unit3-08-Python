# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Oct. 24, 2022
# This program asks the user for a year and then tells them if its a leap year


def main():
    # get year from user
    year = input("Enter a year: ")

    # adds extra line
    print("")

    # try is used to catch miss inputs
    try:
        # checks if the year is evenly divisible by 4
        if int(year) % 4 == 0:
            # checks if the year is not evenly divisible by 100
            # and is evenly divisible by 400
            if not (int(year) % 100 == 0) & int(year) % 400:
                print("Your year is a leap year")
            else:
                print("Your year is not a  leap year")
        else:
            print("Your year is not a leap year")
    except:
        print("Invalid input")


if __name__ == "__main__":
    main()
