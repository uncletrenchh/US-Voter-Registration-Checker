"""
Author: Omoniyi Tomjones
Date: August 26, 2023.
Description: A menu-driven Python application with various functionalities.
"""
import math
import datetime
import string
import random


def generate_secure_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    """
    Generate a secure password based on user preferences.

    Args:
        length (int): Length of the password.
        use_uppercase (bool): Use uppercase letters in the password.
        use_lowercase (bool): Use lowercase letters in the password.
        use_numbers (bool): Use numbers in the password.
        use_special_chars (bool): Use special characters in the password.

    Returns:
        str: Generated password or error message.
    """
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "You must select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def calculate_percentage(numerator, denominator, decimal_points):
    """
    Calculate and format a percentage.

    Args:
        numerator (float): Numerator.
        denominator (float): Denominator.
        decimal_points (int): Number of decimal places.

    Returns:
        str: Formatted percentage.
    """
    try:
        result = (numerator / denominator) * 100
        formatted_result = f'{result:.{decimal_points}f}'
        return formatted_result
    except ZeroDivisionError:
        return "Cannot divide by zero."


def days_until_date(target_date):
    """
    Calculate the number of days until a target date.

    Args:
        target_date (datetime.datetime): Target date.

    Returns:
        int: Number of days until target date.
    """
    today = datetime.datetime.today()
    days_remaining = (target_date - today).days
    return days_remaining


def law_of_cosines(leg_a, leg_b, angle_c):
    """
    Calculate the length of a triangle leg using the Law of Cosines.

    Args:
        leg_a (float): Length of side a.
        leg_b (float): Length of side b.
        angle_c (float): Angle C in degrees.

    Returns:
        float: Length of side c.
    """
    angle_c_rad = math.radians(angle_c)
    c = math.sqrt(leg_a**2 + leg_b**2 - 2 * leg_a * leg_b * math.cos(angle_c_rad))
    return c


def calculate_cylinder_volume(radius, height):
    """
    Calculate the volume of a cylinder.

    Args:
        radius (float): Cylinder radius.
        height (float): Cylinder height.

    Returns:
        float: Cylinder volume.
    """
    volume = math.pi * radius**2 * height
    return volume


def main():
    """
    Main function to drive the menu-driven application.
    Args:
        None.
    Returns:
        None.
    """
    print("Welcome to the Menu-Driven Application!")
    while True:
        print("\nMenu:")
        print("a. Generate Secure Password")
        print("b. Calculate and Format a Percentage")
        print("c. How many days from today until July 4, 2025?")
        print("d. Use the Law of Cosines to calculate the leg of a triangle.")
        print("e. Calculate the volume of a Right Circular Cylinder")
        print("f. Exit program")

        choice = input("Enter your choice: ").lower()

        if choice == 'a':
            length = int(input("Enter the length of the password: "))
            use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
            use_lowercase = input("Use lowercase letters? (y/n): ").lower() == 'y'
            use_numbers = input("Use numbers? (y/n): ").lower() == 'y'
            use_special_chars = input("use special characters? (y/n): ").lower() == 'y'
            password = generate_secure_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
            print("Generated Password:", password)

        elif choice == 'b':
            numerator = float(input("Enter the numerator: "))
            denominator = float(input("Enter the denominator: "))
            decimal_points = int(input("Enter the number of decimal points: "))
            result = calculate_percentage(numerator, denominator, decimal_points)
            print("Formatted Percentage:", result)

        elif choice == 'c':
            target_date = datetime.datetime(2025, 7, 4)
            days_remaining = days_until_date(target_date)
            print("Days until July 4, 2025:", days_remaining)

        elif choice == 'd':
            leg_a = float(input("Enter the length of side a: "))
            leg_b = float(input("Enter the length of side b: "))
            angle_c = float(input("Enter the angle in degrees (angle C): "))
            leg_c = law_of_cosines(leg_a, leg_b, angle_c)
            print("Length of side c:", leg_c)

        elif choice == 'e':
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
            volume = calculate_cylinder_volume(radius, height)
            print("Volume of the cylinder:", volume)

        elif choice == 'f':
            print("Thank you for visiting the application!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ != "__main__":
    pass
else:
    main()
