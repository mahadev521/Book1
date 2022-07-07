class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f'{self.data} | {self.next}'
    
class Stack:
    def __init__(self,maxSize):
        self.head = None
        self.maxSize = maxSize
        self.size = 0
    
    def push(self,val):
        if self.size+1>self.maxSize:
            print('overflow')
            return
        self.size+=1
        print(f'pushed value is {val}')
        if self.head is None:
            self.head=Node(val)
            return 
        
        # cur=self.head
        # while cur.next:
        #     cur=cur.next
        # cur.next=Node(val)
        
        node=Node(val)
        node.next=self.head
        self.head=node
    
    def pop(self):
        if self.size==0:
            print('underflow')
            return
        self.size-=1
        print(f'popped value is {self.head.data}')
        self.head=self.head.next
        # cur=self.head
        # while cur.next.next:
        #     cur=cur.next
        # cur.next=None
    
    def getSize(self):
        return self.size
    
    def isempty(self):
        if self.head is None:
            return 'Stack is empty'
        return 'Stack is not empty'
    
    def reSize(self,newSize):
        self.maxSize=newSize
        
    def display(self):
        # follows lifo
        print(self.head)
        # cur=self.head
        # l=[]
        # while cur:
        #     l.append(str(cur.data))
        #     cur=cur.next

    def getTop(self):
        return self.head.data
    
    def getTail(self):
        cur=self.head
        while cur.next:
            cur=cur.next
        return cur.data
    
    def clear(self):
        self.head=None

stack=Stack(4)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
stack.display()
print(stack.getSize())
print(stack.getTop())
stack.pop()
stack.display()
stack.clear()
stack.display()
