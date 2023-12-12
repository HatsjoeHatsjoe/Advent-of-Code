import numpy as np
from io import StringIO

def create_array_from_txt(filename):
    # Open the input file
    with open(filename, "r") as file:
        # Read all lines in the file
        lines = file.readlines()

    # Create a list to store the numbers
    numbers = []

    # Loop over each line in the file
    for line in lines:
        # Convert the line to a single number
        number = line.strip()

        # Convert the number to a list of digits
        digits = [int(digit) for digit in number]

        # Add the list of digits to the list of numbers
        numbers.append(digits)

    # Convert the list of numbers to a two-dimensional NumPy array
    numbers = np.array(numbers)

    return numbers
    

def look_from_left(data,copy):
    
    for y in range(data.shape[0]):
        highest = -1
        for x in range(data.shape[1]):
            if data[y,x] > highest:
                copy[y,x] = 1
                highest = data[y,x]
    return 

def look_from_right(data,copy):
    
    for y in range(data.shape[0]):
        highest = -1
        for x in range(-1, -data.shape[1]-1, -1):
            if data[y,x] > highest:
                copy[y,x] = 1
                highest = data[y,x]
    return 

def look_from_top(data,copy):
    data_transpose = data.conj().T
    for y in range(data_transpose.shape[0]):
        highest = -1
        for x in range(data_transpose.shape[1]):
            if data_transpose[y,x] > highest:
                copy.T[y,x] = 1
                highest = data_transpose[y,x]
    return 

def look_from_bottom(data,copy):
    data_transpose = data.conj().T
    for y in range(data_transpose.shape[0]):
        highest = -1
        for x in range(-1, -data_transpose.shape[1]-1, -1):
            if data_transpose[y,x] > highest:
                copy.T[y,x] = 1
                highest = data_transpose[y,x]
    return 

def lookfromallsides(data,copy):
    look_from_left(data,copy)
    look_from_right(data,copy)
    look_from_top(data,copy)
    look_from_bottom(data,copy)
    return data

def part_1(namefile):
    data = create_array_from_txt(namefile)
    nrows = len(data)
    ncol  = len(data[0])
    copy = np.zeros((nrows,ncol),dtype=int)
    lookfromallsides(data,copy)
    print('the total amount of trees visible is : ', np.sum(copy))
    return


testdata = create_array_from_txt("2022/data/datadag8_test.txt")

part_1("2022/data/datadag8_2022.txt")

def get_scenic_score(data,row,col):

    maxrow,maxcol = len(data) , len(data[0])

    left = right = up = down = 0

    # to look at the numbers on the RIGHT of currenct number
    for y in data:


    return
