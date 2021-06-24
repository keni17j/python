"""
Module comments.
This is my template.
I referred the PEP8.
"""

import os  # Standard library.
import sys

import numpy as np  # Third party library.
import pandas as pd
from PIL import Image, ImageFilter

import 01_standard  # Local application and library.


def main():
    """
    Explain about this function.
    """

    # Brock comments.
    # Don't write anything obvious.
    # Write correct sentences and not a word.

    # Inline comments.
    # Don't use frequently.
    # Use in effectly case.
    # ex) x = x / 5 # Prevent xxx error.

    # How to name.
    # Class: CapWords.
    # Variable: Lowercase and underscore.
    # Function: Lowercase and underscore.
    # Constant: Uppercase and underscore.

    # Use the single quotation.
    print('Hello')
    # Put "," in the end of lists in the following cases.
    # Case 1: Single tuple.
    # Case 2: Using indents.
    x = [0, 1, 2, 3]
    y = [4]
    y = (4,)
    z = ['zero',
         'one',
         'two',
         'three',
         ]
    # Use white spaces to the lowest priority operator.
    cal = 1 + 2 + 3
    cal = cal + 4*5 - 6
    cal = cal * (7+8) / 9
    a_to_z = 'abcdefg'
             + 'hijklmn'
             + 'opqrstu'
             + 'vwxyz'
    # Slices.
    slice = x[0:1:2]
    slice = x[0 : 1+5 : 2-1]
    # Arguments.
    total = func(1, 2, 3)
    total = func(x=1, y=2, z=3)
    total = func(x=1,
                 y=2,
                 z=3,
                 )
    # Don't write any codes on the same line.
    if total > 0:
        print('Large')
    else:
        print('Small')
    for i in range(3):
        print(i)
    # Use "is" with None, don't use "==".
    if x is None:
        print('None.')
    if x is not None:
        print('Not None.')
    # Don't use the slice when check the first or the end of strings.
    x = 'abcdefg'
    if x.startswith('abc'):
        print('Start with abc')
    if x.endswith('efg'):
        print('End with efg')
    # Seacanse: strings, lists and tuples.
    # Empty seacanse means "False".
    # Don't use "==" with bool.
    x = []
    if not x:
        print('Empty')
    x = ()
    if not x:
        print('Empty')
    x = ""
    if not x:
        print('Empty')


def func(x, y, z):
    """
    Explain about this function.
    """

    total = x + y + z

    return total


if __name__ == '__main__':
    main()
