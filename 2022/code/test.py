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

c = Tree('head')