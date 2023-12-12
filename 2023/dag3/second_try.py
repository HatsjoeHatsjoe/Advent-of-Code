def get_data(filepath):
    with open(filepath, "r") as file:
        content = file.readlines()
    return [line.strip("\n") for line in content]

def loop_all(content):
    ans = 0
    for row in range(len(content)):
        n = 0
        for column in range(len(content[row])):

            if content[row][column].isdigit():
                n = n*10 + int(content[row][column]) 
                            

def main():
    data = get_data('testdata.txt')
    print(data)


if __name__ == '__main__':
    main()