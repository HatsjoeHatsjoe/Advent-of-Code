class Tree:
    # "Generic tree node."
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.files = 0
        self.parent = parent
        self.tot_size = 0

    def add_child(self, node, parent):
        self.children.append(Tree(node,parent))
        

    def add_file(self, file):
        self.files += file


    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child

   
def print_tree(node):
    names = [(node.name,node.files)]

    if  len(node.children) > 0:
        for child in node.children:
            names.append(print_tree(child))
    return names
    
def size_node(node,size):
    
    if len(node.children) == 0:
        node.tot_size = node.files        
        return node , node.tot_size
        
    else:
        for child in node.children:            
            sum_nodes = sum(size_node(child,size)[1]) 
        node.tot_size = Head.files + sum_nodes
         



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
            Current = Current.parent  # parent is nu een string door de manier hoe die is toegevoegd.
                                            # kan vorige map dus niet open op juiste manier.
            
    
        elif x == '$ cd /':
            # hoofdmap aanmaken en die de huidige map maken
            Head = Tree('Head',None)
            Current = Head

        else:
            gesplit = x.split()
            NameChild = gesplit[-1]
            Current = Current.get_child(NameChild)
            
            # 1 van de children de nieuwe 'huidige' map maken
            
                        

    if x[0].isdigit():
        FileSize = x.split()[0]
        FileSize = int(FileSize)
        Current.add_file(FileSize)
        

    if x.startswith('dir'):
        Dirname = x.split()[-1]
        Current.add_child(Dirname,Current)


print(print_tree(Head))
print(size_node(Head,Head.files))
print(sum(size_node(Head,Head.files)))
