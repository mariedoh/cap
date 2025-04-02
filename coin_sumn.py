class Node:
    def __init__(self, options, value, steps):
        self.options = options
        self.value = value
        self.steps = steps
        self.children = []
    
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
            if (check <= 1):
                for_kids = self.options.copy()
                del for_kids[x]
            else:
                for_kids = self.options.copy()
                for_kids[x].pop()
            
            self.children.append(Node(for_kids, new_value, new_steps)) 

        return self.children

class tree_builder:
    def __init__(self, classrooms, value):
        self.head = Node(classrooms, value, [])
        self.level = [self.head]

    def build(self):
        z = []
        for x in self.level:
            q = x.birth()
            z.extend(q)
        self.level= z
        return self.level
    
z = tree_builder({20: ['A', 'B', 'C'], 35: ['D', 'E', 'F', 'G', 'H', 'I'], 40: ['J', 'K']}, 55)
x = []
nonzero = True
while nonzero:
    x = z.build()
    for y in x:
        print(y.get_value())
        if y.get_value() <=0 :
            nonzero = False

min_val = -98765434567
min_node = None
for node in x:
    if node.get_value() > min_val and node.get_value() <= 0:
        min_val = node.get_value()
        min_node = node

print(min_node.get_steps())
