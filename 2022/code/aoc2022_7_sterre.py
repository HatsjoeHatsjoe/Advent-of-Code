import pathlib
import sys


class Node:
    def __init__(self, name, parent, children, size):
        self.parent = parent
        self.children = children  # None if file, [] if folder
        self.name = name
        self.size = size

    def print_node(self, action):
        print(f"'action:{action}'   name: {self.name} parent:{None if self.parent is None else self.parent.name} "
              f"children_len:"
              f"{len(self.children) if self.children else None} size:{self.size}")


def parse(puzzle_input):
    """Parse input"""
    lines = [line.split() for line in puzzle_input.split('\n')]
    i = 0
    current_node = None
    head = None
    for line in lines:
        if line[0] == '$' and line[1] == 'cd':
            if line[2] == '..':
                current_node = current_node.parent
            elif line[2] == '/':
                head = Node('/', None, [], 0)
                current_node = head
            else:
                current_node = [ch for ch in current_node.children if ch.name == line[2]][0]
        elif line[0] == '$' and line[1] == 'ls':
            continue
        elif line[0] == 'dir':
            current_node.children.append(Node(line[1], current_node, [],0))
        else:
            current_node.children.append(Node(line[1], current_node, None, int(line[0])))

    calculate_folder_sizes(head, head.size)
    return head

def calculate_folder_sizes(head, size):
    if head.children is None:
            return head, head.size
    else:
        size_sum = sum([calculate_folder_sizes(child, size)[1] for child in head.children])
        head.size += size_sum
        return head, head.size


def part1(head):
    """Solve part 1"""
    if head.children is None:
        return 0
    total = 0
    if head.size <= 100000:
        total += head.size
    for ch in head.children:
        total += part1(ch)
    return total

def print_tree(head):
    if head.children is None:
        print('File', head.name, 'size', head.size)
    else:
        print('Dir', head.name, 'size', head.size, '[')
        for c in head.children:
            print_tree(c)
        print(']')


def part2(head, delete, list):
    """Solve part 2"""
    # if head.children is None:
    #     return None
    # # print(head.name)
    # if head.size < delete:
    #     print('dir too small:', head.name)
    #     return None
    # print('dir:',head.name)
    # m = head.size
    # for ch in head.children:
    #     x = part2(ch, delete)
    #     print('child:', ch.name, 'size:', x)
    #     if x is not None:
    #         m = min(m,x)
    if head.children is None or head.size < delete:
        # print(head.name, ' is too small or a file')
        return list
    list.append(head.size)
    for ch in head.children:
        list = part2(ch, delete, list)
    # 43956976
    return list



if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()

        head = parse(puzzle_input)

        print("Part 1: ", part1(head))
        print_tree(head)
        print(head.name)
        delete = 30000000- (70000000 - head.size)
        print("Part 2: ", min(part2(head, delete, [])))