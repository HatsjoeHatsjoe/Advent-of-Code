import numpy as np

def openfile(filepath):
    with open(filepath, "r") as file:
        content = file.readlines()
    return [line.strip("\n") for line in content]

def check_neighbors(line, line_below, line_above, torf):
    for index in range(len(line)):
        under = line_below[index] if index < len(line_below) else ''
        above = line_above[index] if index < len(line_above) else ''
        diag_left_below = line_below[index-1] if index > 0 and index < len(line_below) else ''
        diag_right_below = line_below[index+1] if index < len(line)-1 and index < len(line_below) else ''
        diag_left_above = line_above[index-1] if index > 0 and index < len(line_above) else ''
        diag_right_above = line_above[index+1] if index < len(line)-1 and index < len(line_above) else ''

        if line[index].isdigit():
            if (
                not (diag_left_below.isdigit() or diag_left_below in ['.', '']) \
                or not (under.isdigit() or under in ['.', '']) \
                or not (diag_right_below.isdigit() or diag_right_below in ['.', '']) \
                or not (diag_left_above.isdigit() or diag_left_above in ['.', '']) \
                or not (above.isdigit() or above in ['.', '']) \
                or not (diag_right_above.isdigit() or diag_right_above in ['.', ''])
            ):
                torf[index] = 1

    return torf

def sum_numbers_with_adjacent_special(matrix, content):
    total_sum = 0
    for i in range(len(matrix)):
        numbers_row = []
        for j in range(len(matrix[i])):
            if matrix[i, j] == 1:
                # Find the leftmost index of the number
                starting_index = j
                while starting_index > 0 and content[i][starting_index-1].isdigit():
                    starting_index -= 1

                # Collect the full number
                number_str = ''
                while starting_index < len(content[i]) and content[i][starting_index].isdigit():
                    number_str += content[i][starting_index]
                    starting_index += 1

                # Add number to the row if not already present
                if int(number_str) not in numbers_row:
                    numbers_row.append(int(number_str))

        total_sum += sum(numbers_row)
    return total_sum

def check_adjacent(content):
    torf = np.zeros((len(content[0]), len(content)), dtype=int)
    for index in range(len(content)):
        if index == 0:
            torf[index] = check_neighbors(content[index], content[index+1], [], torf=torf[index])
        elif index == len(content)-1:
            torf[index] = check_neighbors(content[index], [], content[index-1], torf=torf[index])
        else:
            torf[index] = check_neighbors(content[index], content[index+1], content[index-1], torf=torf[index])
    return torf

def main():
    content = openfile("data.txt")
    torf = check_adjacent(content=content)
    som = sum_numbers_with_adjacent_special(torf, content)
    print(som)

if __name__ == '__main__':
    main()
