import numpy as np


def main(filepath):
    with open(filepath, 'r') as file:
        content = file.readlines()

    stripped_lines = [x.strip('\n') for x in content]

    total = 0

    for line in stripped_lines:
        number_left = None
        number_right = None

        for character in line:
            if character.isdigit():
                print(character)
                number_left = int(character)
                break

        for character in reversed(line):
            if character.isdigit():
                print(character)
                number_right = int(character)
                break

        whole_number = (number_left*10) + number_right
        print(f"the whole number for this line is: {whole_number}")

        total += whole_number

    print(f"the total at the end is: {total}")


def main2(filepath):
    with open(filepath, 'r') as file:
        content = file.readlines()

    stripped_lines = [x.strip('\n') for x in content]

    numbers_str = ["one", "two", "three", "four",
                   "five", "six", "seven", "eight", "nine"]
    
    total = 0
    numbers_dict = {"one": 1, "two": 2, "three": 3, "four": 4,
                    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    for line in stripped_lines:
        numbers = []

        for index in range(len(line)):
            character = line[index]
            if character.isdigit():
                print(character)
                numbers.append(int(character))
                
            else:
                word1 = line[index:index+3]
                word2 = line[index:index+4]
                word3 = line[index:index+5]
                if word1 in numbers_str:
                    numbers.append(numbers_dict[word1])
                    print(word1)
                elif word2 in numbers_str:
                    numbers.append(numbers_dict[word2])
                    print(word1)
                elif word3 in numbers_str:
                    numbers.append(numbers_dict[word3])
                    print(word1)
        print(f"the variable numbers looks like: {numbers}")
        whole_number = (numbers[0]*10) + numbers[-1]
        print(f"the whole number for this line is: {whole_number}")
        total += whole_number



    print(f"the total at the end is: {total}")


if __name__ == '__main__':
    main("data.txt")
    # main2()
