#!/usr/bin/env python3

import math

"""
Written by: Isak Kjerstad.
Purpose: Calculate distance values needed to build a scale model roof.
Date: 13.07.21
"""

def get_roof_len(angle, floor_len):
    """ Use cosinus to get lenght of roof. """
    return floor_len / math.cos(math.radians(angle))

def get_angle(floor_len, )

def main():

    start_height = int(input("Enter start height: "))
    start_angle = int(input("Enter start angle: "))
    floor_length = int(input("Enter floor length: "))

    roof_length = get_roof_len(start_angle, floor_length)

    print(roof_length)
    

if __name__ == "__main__":
    main()