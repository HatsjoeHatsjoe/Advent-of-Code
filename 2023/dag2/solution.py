def getcontent(filepath: str):
    with open(filepath, 'r') as file:
        content = file.readlines()
    return content


def splitgames1(content):
    elligable_id = []
    for line in content:
        stripped_line = line.strip("\n")
        sets = stripped_line.split(";")
        # print(sets)
        elligable = True
        my_id = None
        for set in sets:
            red, blue, green = 0, 0, 0
            words = set.split()

            if set == sets[0]:
                my_id = int(words[1].strip(':'))

            for index in range(len(words)):
                if words[index] in ['red', 'red,']:
                    red += int(words[index-1])
                elif words[index] in ['blue', 'blue,']:
                    blue += int(words[index-1])
                elif words[index] in ['green', 'green,']:
                    green += int(words[index-1])
                else:
                    continue
            # print(f"the total of red looks like: {red}")
            # print(f"the total of blue looks like: {blue}")
            # print(f"the total of green looks like: {green}")

            if red >= 13 or green >= 14 or blue >= 15:
                elligable = False

        if elligable:
            elligable_id.append(my_id)

    print(elligable_id)
    print(f"som: {sum(elligable_id)}")


def splitgames2(content):
    all_powers = []
    for line in content:
        stripped_line = line.strip("\n")
        sets = stripped_line.split(";")
        # print(sets)
        red, blue, green = 0, 0, 0
        for set in sets:
            words = set.split()
            for index in range(len(words)):
                if words[index] in ['red', 'red,']:
                    if int(words[index-1]) > red:
                        red = int(words[index-1])
                elif words[index] in ['blue', 'blue,']:
                    if int(words[index-1]) > blue:
                        blue = int(words[index-1])
                elif words[index] in ['green', 'green,']:
                    if int(words[index-1]) > green:
                        green = int(words[index-1])
                else:
                    continue

            # print(f"the max of red looks like: {red}")
            # print(f"the max of blue looks like: {blue}")
            # print(f"the max of green looks like: {green}")

        power = red*green*blue
        # print(f"The power is : {power}")
        all_powers.append(power)

    print(all_powers)
    print(f"som van powers: {sum(all_powers)}")


def main():
    content = getcontent('data.txt')
    splitgames1(content=content)
    splitgames2(content=content)


if __name__ == '__main__':
    main()
