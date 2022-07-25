class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f'{self.data} {self.next}'
    
class Stack:
    def __init__(self):
        self.head = None
    
    def push(self,val):
        if self.head is None:
            self.head=Node(val)
            return 
        node=Node(val)
        node.next=self.head
        self.head=node
    def pop(self):
        x=self.head.data
        self.head=self.head.next
        return x
    
    def isempty(self):
        return self.head is None
    
    def peek(self):
        return self.head.data
    
    def clear(self):
        self.head=None
    
    def display(self):
        x=str(self.head)
        return x

def isBalanced(x):
    stack=Stack()
    for i in x:
        if i=='(':
            stack.push(i)
        elif i==')':
            if stack.isempty():
                return False
            else:
                stack.pop()
    return stack.isempty()
    


x=input()
print(isBalanced(x))