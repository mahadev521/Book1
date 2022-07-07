'''doubly linked listimplementation'''

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return f'{self.data} <-> {self.next}'
class Dll:
    def __init__(self, head=None):
        self.head = head
        self.length = 0
    
    def addnode(self, node):
        node=Node(node)
        if self.head is None:
            self.head = node
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=node
            node.prev=cur
        self.length+=1
    
    def extend(self,arr):
        if self.head == None:
            self.head = Node(arr[0])
            self.length+=1
            cur=self.head
            prev=None
            for i in arr[1:]:
                self.length+=1
                cur.next=Node(i)
                cur.prev=prev
                prev=cur.next
                cur=cur.next
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            for i in arr:
                self.length+=1
                temp=Node(i)
                cur.next=temp
                temp.prev=cur
                cur=cur.next
    
    def ibegin(self,node):
        node=Node(node)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node
        self.length+=1
    
    def iend(self,node):
        self.addnode(node)
    
    def iatpos(self,node,pos):
        if pos<0 or pos>self.length+1:
            print('insertion not possible')
            return
        if pos==1: 
            self.ibegin(node)
            return
        if pos==self.length+1:
            self.iend(node)
            return
        count=2
        cur=self.head
        while cur:
            if count==pos:
                self.length+=1
                '''order ncp'''
                node=Node(node)
                #first initialize the next node
                node.next=cur.next
                #initialize current node
                cur.next=node
                #initialize previous node
                node.prev=cur
                return
            cur=cur.next
            count+=1
    
    def getvalue(self,pos):
        pos-=1
        if pos>self.length:
            return 'cannot get value'
        cur=self.head
        for _ in range(pos):
            cur=cur.next
        return cur.data
    
    def reverse(self):
        cur=self.head
        prev=None
        while cur:
            next=cur.next
            cur.next=prev
            cur.prev=next
            prev=cur
            cur=next
        self.head=prev
    
    def __str__(self):
        return f'{self.head}'

# node=Node(45)
# dll=Dll(node)
# dll.addnode(Node(46))
# dll.addnode(Node(47))
# print(dll)

dll=Dll()
dll.extend([1,2,3,11,4,5,6])
print(dll)
dll.reverse()
print(dll)
# print(dll.getvalue(6))
# print(dll.head)

# dll.extend([11,12,13])
# dll.addnode(14)
# print(dll)
# dll.ibegin(78)
# print(dll)
# dll.iend(100)
# print(dll)
# print(dll.length)
# dll.iatpos(99,5)
# print(dll)