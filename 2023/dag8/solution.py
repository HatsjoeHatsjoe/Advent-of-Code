from math import gcd
def get_data(filepath):
    with open(filepath,"r") as file:
        content = file.readlines()
    str_content = [x.strip('\n') for x in content]
    instructions = str_content[0]
    path = str_content[2:]
    # print(str_content)
    return instructions , path

def next_step(current_point, all_paths, instruction):
    for x in all_paths:
        if x.startswith(current_point):
            losse = x.split()
            # print(x)
            if instruction =='L':
                return losse[2].strip('(').strip(',')
            elif instruction == 'R':
                return losse[-1].strip(')')
            else:
                raise ValueError


def main1():
    instructions, full_path = get_data("data.txt")
    # print(full_path)
    first_step = "AAA"
    index_instr = 0
    current_string = first_step
    count = 0
    while current_string != 'ZZZ':
        if index_instr == len(instructions):
            index_instr = 0
        volgende = next_step(current_string, full_path, instructions[index_instr])
        # print(f"current string is {current_string}, The step instruction says we should go {instructions[index_instr]} Thus resulting in the next step: {volgende}")
        index_instr += 1
        current_string = volgende
        count += 1
    print(count)

def get_startingpoints(all_paths):
    starting_nodes = []
    for x in all_paths:
        if x[2] =='A':
            starting_nodes.append(x[:3])
    return starting_nodes

def lcm(xs):
    ans = 1
    for x in xs:
        ans = (ans*x)//gcd(x,ans)
    return ans

def main2():
    instructions, full_path = get_data("data.txt")
    starting_nodes = get_startingpoints(full_path)
    print(starting_nodes)
    
    loops = []
    for node in starting_nodes:
        current_node = node
        index_instr = 0
        count = 0
        while not current_node.endswith('Z'):
            if index_instr == len(instructions):
                index_instr = 0
            volgende = next_step(current_node,full_path,instruction=instructions[index_instr])
            index_instr += 1
            current_node = volgende
            count += 1
        loops.append(count)

    print(lcm(loops))

if __name__ == '__main__':
    main2()