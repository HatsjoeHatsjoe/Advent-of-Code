import csv
import numpy as np

def openfile(filepath):
    with open(filepath, "r") as file:
        content = file.readlines()
    return [line.strip("\n") for line in content]

def save_matrix_to_csv(matrix, filepath):
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(matrix)

def look_below(line, line_below, torf):
    for index in range(len(line)):
        under = line_below[index]
        diag_left = line_below[index-1] if index > 0 else ''
        diag_right = line_below[index+1] if index < len(line)-1 else ''

        if line[index].isnumeric():
            if not (diag_left.isnumeric() or diag_left in ['.', '']) \
                    or not (under.isnumeric() or under in ['.', '']) \
                    or not (diag_right.isnumeric() or diag_right in ['.', '']):
                torf[index] = 1

    return torf

def same_row(line, torf):
    for index in range(len(line) - 1):  # Fix indexing issue here
        volgende = line[index+1]
        vorige = line[index-1] if index > 0 else ''

        if line[index].isnumeric():
            if not (vorige.isnumeric() or vorige in ['.', '']) \
                    or not (volgende.isnumeric() or volgende in ['.', '']):
                torf[index] = 1
    return torf

def look_above(line, line_above, torf):
    for index in range(len(line)):
        above = line_above[index]
        diag_left = line_above[index-1] if index > 0 else ''
        diag_right = line_above[index+1] if index < len(line)-1 else ''

        if line[index].isnumeric():
            if not (diag_left.isnumeric() or diag_left in ['.', '']) \
                    or not (above.isnumeric() or above in ['.', '']) \
                    or not (diag_right.isnumeric() or diag_right in ['.', '']):
                torf[index] = 1

    return torf


def check_adjecent(content):
    torf = np.zeros((len(content[0]), len(content)), dtype=int)
    for index in range(len(content)):
        if index == 0:
            torf[index] = look_below(content[index], content[index+1], torf=torf[index])
            torf[index] = same_row(content[index], torf=torf[index])
        elif index == len(content)-1:
            torf[index] = look_above(content[index], content[index-1], torf=torf[index])
            torf[index] = same_row(content[index], torf=torf[index])
            # save_matrix_to_csv(torf,filepath='torf_matrix.csv')
        else:
            torf[index] = same_row(content[index], torf=torf[index])
            torf[index] = look_below(content[index], content[index+1], torf=torf[index])
            torf[index] = look_above(content[index], content[index-1], torf=torf[index])
    
    return torf

def sum_numbers_with_adjacent_special(matrix, content):
    total_sum = 0
    for i in range(len(matrix)):
        numbers_row = []
        for j in range(len(matrix[i])):
            if matrix[i, j] == 1:
                # Find the leftmost index of the number
                starting_index = j
                while starting_index > 0 and content[i][starting_index-1].isnumeric():
                    starting_index -= 1

                # Collect the full number
                number_str = ''
                while starting_index < len(content[i]) and content[i][starting_index].isnumeric():
                    number_str += content[i][starting_index]
                    starting_index += 1

                # Add number to the row if not already present
                if int(number_str) not in numbers_row:
                    numbers_row.append(int(number_str))
                else:
                    print(f'found same number in row {i+1}, at position {j+1}')

        total_sum += sum(numbers_row)
        print(f"For row {i+1} , the total amount of elligable numbers is: {len(numbers_row)} and the whole list looks like: {numbers_row}.\nThe total at this point is: {total_sum}")
    return total_sum


def main1():
    content = openfile("data.txt")
    torf = check_adjecent(content=content)
    som = sum_numbers_with_adjacent_special(torf, content)
    print(som)
    print(torf)
    return torf


########################################################################################################

def check_adjecent2(content):
    torf = np.zeros((len(content), len(content[0])), dtype=int)

    for i in range(len(content)):
        for j in range(len(content[i])):
            current_char = content[i][j]

            # Check if the current character is a digit
            if current_char.isdigit():
                above = content[i - 1][j] if i > 0 else ''
                below = content[i + 1][j] if i < len(content)-1 else ''
                left = content[i][j - 1] if j > 0 else ''
                right = content[i][j + 1] if j < len(content[i])-1 else ''

                diag_left_up = content[i - 1][j - 1] if (i > 0 and j > 0) else ''
                diag_right_up = content[i - 1][j + 1] if (j < len(content[i])-1 and i > 0) else ''
                diag_left_down = content[i + 1][j - 1] if (j > 0 and i < len(content)-1) else ''
                diag_right_down = content[i + 1][j + 1] if (j < len(content[i])-1 and i < len(content)-1) else ''

                # Check if any adjacent or diagonal character is a special character
                if (
                    below in ('*', '+', '&', '#', '@', '=', '/', '%', '$', '-') or
                    above in ('*', '+', '&', '#', '@', '=', '/', '%', '$', '-') or
                    left in ('*', '+', '&', '#', '@', '=', '/', '%', '$', '-') or
                    right in ('*', '+', '&', '#', '@', '=', '/', '%', '$', '-') or
                    diag_left_up in ('*', '+', '&', '#', '@', '=', '/', '%', '$', '-') or
                    diag_right_up in ('*', '+', '&', '#', '@', '=', '/', '%', '$', '-') or
                    diag_left_down in ('*', '+', '&', '#', '@', '=', '/', '%', '$', '-') or
                    diag_right_down in ('*', '+', '&', '#', '@', '=', '/', '%', '$', '-')
                ):
                    torf[i, j] = 1

    return torf

def check_adjecent3(content):
    torf = np.zeros((len(content), len(content[0])), dtype=int)
    special_chars = {'*', '+', '&', '#', '@', '=', '/', '%', '$', '-'}

    for i in range(len(content)):
        for j in range(len(content[i])):
            current_char = content[i][j]

            if current_char.isdigit():
                # Relative positions of adjacent and diagonal cells
                positions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                             (-1, -1), (-1, 1), (1, -1), (1, 1)]

                for di, dj in positions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(content) and 0 <= nj < len(content[i]):
                        if content[ni][nj] in special_chars:
                            torf[i, j] = 1
                            break

    return torf


def main3():
    content = openfile("data.txt")
    torf = check_adjecent2(content=content)
    # print(torf)
    torf2 = check_adjecent3(content=content)
    # if np.array_equal(torf, torf2):
    #     print("they are the same")
    som = sum_numbers_with_adjacent_special(torf2,content=content)
    print(som)
    return torf2

if __name__ == '__main__':
    torf1 = main1()
    print("\nNieuwe begint hier:\n\n")
    torf2 = main3()
    if np.array_equal(torf1, torf2):
        print("they are the same")
