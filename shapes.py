# Author: Cuong Le
# Date: 09/30/2026
# Course: Coding with AI
# This program calculates the areas and circumference of common shapes.

import math


# Calculates the area of a square.
def area_of_square(side):
    return side ** 2


# Calculates the area of a rectangle.
def area_of_rectangle(length, width):
    return length * width


# Calculates the area of a triangle.
def area_of_triangle(base, height):
    return (base * height) / 2


# Calculates the area of a circle using pi.
def area_of_circle(radius):
    return math.pi * radius ** 2


# Calculates the circumference of a circle using pi.
def circumference_of_circle(radius):
    return 2 * math.pi * radius


# Displays the menu and handles the user's selections.
def main():
    while True:
        # Show the available calculations.
        print("\nShape Calculator")
        print("1. Area of a square")
        print("2. Area of a rectangle")
        print("3. Area of a triangle")
        print("4. Area of a circle")
        print("5. Circumference of a circle")
        print("6. Exit")

        # Strip whitespace so entries like " 1 " are accepted.
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Calculate the area of a square.
            try:
                side = float(input("Enter the side length: "))
                # Check that the measurement is positive before calculating.
                if side <= 0:
                    print("Measurements must be greater than zero.")
                else:
                    print(f"Area: {area_of_square(side):.2f}")
            except ValueError:
                # Handle non-numeric measurement input.
                print("Invalid input. Please enter a numeric value.")
        elif choice == "2":
            # Calculate the area of a rectangle.
            try:
                length = float(input("Enter the length: "))
                width = float(input("Enter the width: "))
                if length <= 0 or width <= 0:
                    print("Measurements must be greater than zero.")
                else:
                    print(f"Area: {area_of_rectangle(length, width):.2f}")
            except ValueError:
                # Handle non-numeric measurement input.
                print("Invalid input. Please enter a numeric value.")
        elif choice == "3":
            # Calculate the area of a triangle.
            try:
                base = float(input("Enter the base: "))
                height = float(input("Enter the height: "))
                if base <= 0 or height <= 0:
                    print("Measurements must be greater than zero.")
                else:
                    print(f"Area: {area_of_triangle(base, height):.2f}")
            except ValueError:
                # Handle non-numeric measurement input.
                print("Invalid input. Please enter a numeric value.")
        elif choice == "4":
            # Calculate the area of a circle.
            try:
                radius = float(input("Enter the radius: "))
                if radius <= 0:
                    print("Measurements must be greater than zero.")
                else:
                    print(f"Area: {area_of_circle(radius):.2f}")
            except ValueError:
                # Handle non-numeric measurement input.
                print("Invalid input. Please enter a numeric value.")
        elif choice == "5":
            # Calculate the circumference of a circle.
            try:
                radius = float(input("Enter the radius: "))
                if radius <= 0:
                    print("Measurements must be greater than zero.")
                else:
                    print(
                        f"Circumference: "
                        f"{circumference_of_circle(radius):.2f}"
                    )
            except ValueError:
                # Handle non-numeric measurement input.
                print("Invalid input. Please enter a numeric value.")
        elif choice == "6":
            # Exit the program.
            print("Bye!")
            break
        else:
            # Handle menu choices outside 1 through 6.
            print("Invalid choice. Please enter a number from 1 to 6.")


# Run the calculator when this file is executed directly.
if __name__ == "__main__":
    main()