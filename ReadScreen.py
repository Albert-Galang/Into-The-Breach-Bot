import os
import time

from numpy import *
import win32api
import win32con
from PIL import ImageGrab, ImageOps

box_x = 24
box_y = 18

tiles = {'mountain': 26964,
         'civ': 24780,
         'civ 2': 25896,
         'ground': 31104
         }


def read_tile(x, y):
    """
    Get screenshot from the primary monitor from which we'll extract info
    :return:
    """
    # TODO: Look into greyscale vs RGB (maybe easier to distinguish tiles)
    box = (x, y, x+box_x, y+box_y)
    image = ImageOps.grayscale(ImageGrab.grab(box))
    grab_sum = sum(array(image))
    print(grab_sum)
    # image.show()
    return grab_sum


def read_column(x, y):
    horizontal_shift = 84
    vertical_shift = 63
    i = 0

    column_vals = []

    while i < 8:
        shifted_x = x
        shifted_y = y
        shifted_x -= (horizontal_shift * i)
        shifted_y -= (vertical_shift * i)
        print('x is', shifted_x, 'y is', shifted_y)
        column_vals.append(read_tile(shifted_x, shifted_y))
        i += 1
    return column_vals


def translate_board():
    origin_x = 947
    origin_y = 966
    horizontal_shift = 84
    vertical_shift = 63
    i = 0
    board = []

    while i < 8:
        x = origin_x + (horizontal_shift * i)
        y = origin_y - (vertical_shift * i)
        board.append(read_column(x, y))
        i += 1

    return board


def main():
    board = translate_board()
    print(board)


'''
middle of the board 958
square dimensions 103 x 103 

1031, 151, 1031+25, 151+21

h8 = 947, 84, 947+24, 84+18
a1 = 947, 966, 947+24, 966+18

84 + 630 = 714

new mountain = 1115, 714, 1115+24, 713+18
attempt = 1199, 777, 1199+24, 777+18 

the down shift is 126
the right shift is 1115 - 947 = 168
its just a half shift for diagonals

diagonal h8 to h1 is 735 which is a 105 shift
1535, 525, 1535+25, 525+18

mountain = 26964

shift to the right by 126?
947, 210, 947+24, 210+18


'''

if __name__ == '__main__':
    main()
