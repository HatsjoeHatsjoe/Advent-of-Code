def get_data(filepath):
    with open(filepath, "r") as file:
        content = file.readlines()
    return [line.strip("\n") for line in content]

def part1(data):
    totaalsom = 0
    for line in data:
        spl_line = line.split()
        current_step = [int(x) for x in spl_line]
        end_list = []
        while any(item != 0 for item in current_step):
            tmp_list = [
                current_step[index + 1] - current_step[index]
                for index in range(len(current_step) - 1)
            ]
            end_list.append(current_step[-1])
            current_step = tmp_list
            # print(tmp_list)
        # print(end_list)

        totaalsom += sum(end_list)

    print(totaalsom)

def part2(data):
    totaalsom = 0
    for line in data:
        spl_line = line.split()
        current_step = [int(x) for x in spl_line]
        begin_list = []
        while any(item != 0 for item in current_step):
            tmp_list = [
                current_step[index + 1] - current_step[index]
                for index in range(len(current_step) - 1)
            ]
            begin_list.append(current_step[0])
            current_step = tmp_list
            # print(tmp_list)
        # print(begin_list)
        begin_list.append(0)
        number = 0
        for x in range(len(begin_list)-1,0,-1):
            number = begin_list[x-1] - number
            # print(number)

        totaalsom += number

    print(totaalsom)

def main():
    data = get_data("data.txt")
    part1(data)
    part2(data)
    






if __name__ == "__main__":
    main()