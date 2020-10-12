"""This module helps you work with matrix
"""

from random import randint as rand

def printMx(matrix):
    """Printing a matrix

    agrs:
    matrix - matrix you want to print

    """
    print()
    print("MATRIX".center(len(matrix[0])*3, "-"))
    for i in matrix:
        print(i)
    print()

def genMx(matrix_width, matrix_height, value_from, value_to, repeat_possible):
    """Generates a matrix

    args:
    matrix_width, matrix_height - lenght of matrix and string of matrix respectively
    value_from, value_to - values of your matrix are in range[value_from,value_to]
    repeat_possible - if True, elements of your matrix might repeat

    """

    if matrix_height == 0 or matrix_width == 0:
        raise ValueError("Matrix sizes cannot equal to zero")
    if value_from > value_to:
        raise ValueError("Lower value cannot be more than upper value")
    if not repeat_possible:
        if value_to - value_from + 1 < matrix_height*matrix_width:
            raise ValueError("Range of values is not enough to fill matrix")
    matrix = []
    row = []
    elements = []
    for r in range(matrix_height):
        row = []
        for i in range(matrix_width):
            a = rand(value_from, value_to)
            if not repeat_possible:
                while a in elements:
                    a = rand(value_from, value_to)
            row.append(a)
            elements.append(a) 
        matrix.append(row)
    return matrix
    
def elements(matrix):
    """Returns list of elements in matrix

    args:
    matrix 

    Each element added in list once, even if it repeated in matrix

    """

    elements = []
    for i in matrix:
        for m in i:
            if m not in elements:
                elements.append(m)
    return elements
