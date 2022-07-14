#!/usr/bin/env python3

import math

"""
Written by: Isak Kjerstad.
Purpose: Calculate distance values needed to build a scale model roof.
Date: 14.07.21
"""

def get_roof_height(angle, normal_len):
    """ Use tangent to find the roof height in any given point. """
    return normal_len * math.tan(math.radians(angle))

def get_roof_len(floor_len, delta_h):
    """ Use the Pythagorean theorem to get the length of a roof section. """
    return math.sqrt(delta_h * delta_h + floor_len * floor_len)

def get_roof_angle(floor_len, delta_h):
    """ Use tangent inverse to find angle of roof sections. """
    try:
        return math.degrees(math.atan(delta_h / floor_len))
    except ZeroDivisionError:
        return 0

def new_measurement(choice):
    """ Check if user requested another measurement. """

    yes = ["y", "Y", "yes", "YES"]

    if choice in yes:
        return True
    else:
        return False

def main():

    # Set initial building parameters.
    start_height = float(input("Enter roof start height (m): "))
    roof_angle = float(input("Enter roof angle (deg): "))

    print("\nRoof starts at {} meters with a {} degree tilt.".format(start_height, roof_angle))

    while True:

        # Ask the user for input for the given roof section.
        floor_len = float(input("\nEnter distance of X (m): "))
        l1 = float(input("Enter length L1 (m): "))
        l2 = float(input("Enter length L2 (m): "))

        # Calculate height of two points on the roof.
        h1 = get_roof_height(roof_angle, l1) + start_height
        h2 = get_roof_height(roof_angle, l2) + start_height

        delta_h = h2 - h1

        # Get length and angle of the roof section.
        roof_len = get_roof_len(floor_len, delta_h)
        roof_angle = get_roof_angle(floor_len, delta_h)

        # Display result to the user.
        print("\n")
        print("Roof section length:  {0:.3f} meters.".format(roof_len))
        print("Roof section tilt:    {0:.3f} degrees.".format(roof_angle))
        print("Height of L1 end:     {0:.3f} meters.".format(h1))
        print("Height of L2 end:     {0:.3f} meters.".format(h2))
        print("Height difference:    {0:.3f} meters.".format(delta_h))
        print("\n")

        # Prompt for program exit or a new measurment.
        if not new_measurement(input("New measurement (y/n): ")):
            break

if __name__ == "__main__":
    main()