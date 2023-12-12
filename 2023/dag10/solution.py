def get_data(filepath):
    with open(filepath, "r")as file:
        content = file.readlines()
    return [list(line.strip('\n')) for line in content]


def main():
    grid = get_data(filepath="testdata1.txt")
    

if __name__ == '__main__':
    main()