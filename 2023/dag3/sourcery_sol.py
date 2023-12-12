import re

def check_number_connected_to_special(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()

    matrix = []
    for line in content:
        row = []
        for char in line.strip():
            if char.isdigit():
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)

    total_sum = 0
    for i in range(len(matrix)):
        numbers_set = set()
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                # Find adjacent, diagonal, and vertical special characters
                adjacent_chars = ''.join([
                    content[i-1][j] if i > 0 else '',
                    content[i+1][j] if i < len(content)-1 else '',
                    content[i][j-1] if j > 0 else '',
                    content[i][j+1] if j < len(content[i])-1 else '',
                    content[i-1][j-1] if i > 0 and j > 0 else '',
                    content[i-1][j+1] if i > 0 and j < len(content[i])-1 else '',
                    content[i+1][j-1] if i < len(content)-1 and j > 0 else '',
                    content[i+1][j+1] if i < len(content)-1 and j < len(content[i])-1 else ''
                ])
                
                # Find numbers adjacent to special characters using regular expression
                for match in re.finditer(r'\d+', adjacent_chars):
                    number = int(match.group())
                    numbers_set.add(number)
        
        total_sum += sum(numbers_set)
        print(f"For row {i+1}, the total amount of eligible numbers is: {len(numbers_set)} and the whole list looks like: {list(numbers_set)}.\nThe total at this point is: {total_sum}")
    return total_sum


file_path = r'c:\Users\ezrae\OneDrive\Documenten\GitHub\Advent-of-Code\2023\dag3\testdata.txt'
result = check_number_connected_to_special(file_path)
print(f"The total sum of eligible numbers is: {result}")
