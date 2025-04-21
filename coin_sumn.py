import copy
class Node:
    def __init__(self, options, value, steps):
        self.options = options
        self.value = value
        self.steps = steps
        self.children = []
    def get_options(self):
        return self.options
    def get_value(self):
        return self.value
    def get_steps(self):
        return self.steps
    def birth(self):
        for x in self.options:
            x= int(x)
            new_value = self.value - x
            new_steps = self.steps + [x]
            check = len(self.options[x])
            for_kids = copy.deepcopy(self.options)

            if (check <= 1):
                del for_kids[x]
            else:
                for_kids[x].pop()
            
            self.children.append(Node(for_kids, new_value, new_steps)) 

        return self.children

class tree_builder:
    def __init__(self, classrooms, value):
        self.head = Node(classrooms, value, [])
        self.level = [self.head]

    def build(self):
        z = []
        values = {}
        val = False
        for x in self.level:
            q = x.birth()
            for y in q:
                if y.get_value() not in values:
                    z.append(y)
                    values[y.get_value()] = "here"
                    if(y.get_value() <= 0):
                        val = True
        self.level= z
        return [self.level, val]

def tree_user(classrooms, value): 
    space =   sum([x * len(classrooms[x]) for x in classrooms])
    if(space < value):
        print("VALUE TOO LARGE",space, value)
        return False 
    z = tree_builder(classrooms, value)
    x = []
    nonzero = True

    while nonzero:
        x = z.build()
        nonzero = not x[1] 
    min_val = -98765434567
    min_node = None
    for node in x[0]:
        if node.get_value() > min_val and node.get_value() <= 0:
            if min_node != None and len(node.get_steps()) >= len(min_node.get_steps()):
                pass                 
            else:       
                min_val = node.get_value()
                min_node = node
    return(min_node.get_steps())

print(tree_user({20: ['A', 'B', 'C'], 35: ['D', 'E', 'F', 'G', 'H', 'I'], 40: ['J', 'K']}, 195))

