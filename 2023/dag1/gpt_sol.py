# def extract_calibration_value(line):
#     # Extract the first and last digits and form a two-digit number
#     first_digit = int(line[0])
#     last_digit = int(line[-1])
#     return first_digit * 10 + last_digit

# def sum_calibration_values(calibration_input):
#     # Split the input into lines and calculate the sum of calibration values
#     lines = calibration_input.split("\n")
#     total_sum = 0

#     for line in lines:
#         # Skip empty lines
#         if line:
#             calibration_value = extract_calibration_value(line)
#             total_sum += calibration_value

#     return total_sum

# # Your large input
# calibration_input = '''
# tmmnhlxzpj1eightldxhjnone97
# 9fivekfpl855mjmfdqzvbn
# two29eighteight1
# 4md
# sixbrqklb347
# 6sevenninexpnbgbr11three15
# 4zggkljkcqthree7
# 7lxjkqhmxcxsevennhszsbxzdfsonehnsrcfour9
# jtpmfoureightvtjmlshbfour6nvjkqnddp3
# twofive2fourfive1dvnrrvjr
# twoeightnq6ninepxv
# 39sixgphfvninexts71five
# seven3two8
# six59jhtfvv1five6
# 7871three915
# prrvrjlpgxpjdxfchqonepchqbhqxx9nbrvh
# gneightwo5txxzpkctwojvrcgbd9
# 329
# 5mnmpsevenseven
# ccshz8
# threeqthree5eight6blzzh
# moneight3onepkjskr9
# ctdk8zkhzzkt
# nbfrmvlnmbeightbxs55
# six5mrrvsxqhqj162sevenntsnztmsdbnine
# 78dlfqtsplmnbrtfive3tskrrjnqktrkrfdxps
# rljhmtwotwo5sevenfourtwo
# 6drnzxz9fourfourfourxfxsxhlzqx
# 7two8dvhghtd
# five277
# four7mfhfcpqjjvlxvbs
# sixhdxxhrzrsjthree2zddffivevzkcppvpshh
# hnsnbldnp5hdfzqnine
# kbdfmgjtfxzszl6fourtwo72eight
# 4fourxrtvjh
# dzbfkvzlg6ngnrsevenzfqmlldc7
# eighthg62txtxhkl9
# 5dckmbonetwolgsixvvftfive
# '''

# # Calculate and print the sum of calibration values
# result = sum_calibration_values(calibration_input)
# print("Sum of calibration values:", result)

###########################################################################################################################
def extract_calibration_value(line):
    # Extract the first and last digits and form a two-digit number
    digits = [char for char in line if char.isdigit()]
    
    if len(digits) >= 2:
        first_digit = int(digits[0])
        last_digit = int(digits[-1])
        return first_digit * 10 + last_digit
    else:
        return 0  # Return 0 if there are not enough digits

def sum_calibration_values(calibration_input):
    # Split the input into lines and calculate the sum of calibration values
    lines = calibration_input.split("\n")
    total_sum = 0

    for line in lines:
        # Skip empty lines
        if line:
            calibration_value = extract_calibration_value(line)
            total_sum += calibration_value

    return total_sum

# Read data from the file
file_path = "data.txt"
with open(file_path, "r") as file:
    calibration_input = file.read()

# Calculate and print the sum of calibration values
result = sum_calibration_values(calibration_input)
print("Sum of calibration values:", result)

###################??
def extract_calibration_value_part2(line):
    # Define a dictionary mapping spelled-out numbers to digits
    number_mapping = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    # Extract the real first and last digits on each line
    words = line.split()
    first_digit = int(''.join([number_mapping.get(word, word) for word in ''.join(words[0]).split() if word.isalnum()]))
    last_digit = int(''.join([number_mapping.get(word, word) for word in ''.join(words[-1]).split() if word.isalnum()]))
    return first_digit * 10 + last_digit

def sum_calibration_values_part2(calibration_input):
    # Split the input into lines and calculate the sum of calibration values
    lines = calibration_input.split("\n")
    total_sum = 0

    for line in lines:
        # Skip empty lines
        if line:
            calibration_value = extract_calibration_value_part2(line)
            total_sum += calibration_value

    return total_sum

# Read data from the file
file_path = "data.txt"
with open(file_path, "r") as file:
    calibration_input = file.read()

# Calculate and print the sum of calibration values for Part 2
result_part2 = sum_calibration_values_part2(calibration_input)
print("Part 2 - Sum of calibration values:", result_part2)
