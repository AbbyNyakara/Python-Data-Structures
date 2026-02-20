class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def push(self, value):
        return self.stack_list.append(value)
    
    def pop(self):
        return self.stack_list.pop()
    
    def is_empty(self):
        return len(self.stack_list) == 0
    

def reverse_string(string):
    new_stack = Stack()

    for char in string:
        new_stack.push(char)
    
    reversed_list = []

    while not new_stack.is_empty():
        reversed_list.append(new_stack.pop())

    return "".join(reversed_list)


print(reverse_string(""))

    



