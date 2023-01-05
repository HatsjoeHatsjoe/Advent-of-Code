class Tree:
    # "Generic tree node."
    def __init__(self, name):
        self.name = name
        self.children = []
        self.files = 0
        self.parent = []

    def add_child(self, node):
        self.children.append(Tree(node))
        

    def add_file(self, file):
        self.files += file


    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child

    def get_parent(self):
        for parent in self.parent:
            return parent
    
    

def print_tree(node):
    if not node.children:
        return node.name , node.files
    
    else:
        nieuw = print_tree(node)
        return nieuw
        
            



file1 = open('2022/data/datadag7_2022.txt','r')
lines = file1.readlines()

data = []
for x in lines:
    data.append(x.replace('\n',''))
    file2 = open('2022/data/testdata_dag7.txt','r')


lines2 = file2.readlines()

data2 = []
for x in lines2:
    data2.append(x.replace('\n',''))

data = data2

print(data)


for x in data:
    if x.startswith('$ cd'):
        # print('er stond cd')
        if x[-1] == '.':
            print(Current.parent)
            Current = Current.get_parent()
            
    
        elif x == '$ cd /':
            # hoofdmap aanmaken en die de huidige map maken
            Head = Tree('Head')
            Current = Head

        else:
            gesplit = x.split()
            NameChild = gesplit[-1]
            Temp_Parent = Current.name
            Current = Current.get_child(NameChild)
            Current.parent = Temp_Parent
            
            # 1 van de children de nieuwe 'huidige' map maken
            # ook de parent van de nieuwe map definieren
                        

    if x[0].isdigit():
        FileSize = x.split()[0]
        FileSize = int(FileSize)
        Current.add_file(FileSize)
        

    if x.startswith('dir'):
        Dirname = x.split()[-1]
        Current.add_child(Dirname)


   