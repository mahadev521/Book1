class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None
    
    def __str__(self):
        return f'{self.val} -> {self.next}'

class Queue:
    def __init__(self,maxSize):
        self.head = None
        self.tail = None
        self.maxSize = maxSize
        self.size = 0
    
    def enqueue(self,val):
        if self.size+1>self.maxSize:
            print('Overflow condition')
            return
        self.size += 1
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
            return
        self.tail.next=Node(val)
        self.tail=self.tail.next
    
    def dequeue(self):
        if not self.head:
            print('underflow condition detected')
            return
        self.size -= 1
        cur = self.head
        self.head = self.head.next
        print(f'removed {cur.val}')
    
    
    def rotate(self,k):
        cur=self.head
        length=1
        while cur.next:
            cur=cur.next
            length+=1
        cur.next=self.head
        if k>length:
            k=k%length
        k=length-k
        for _ in range(k):
            cur=cur.next
        self.head=cur.next
        self.tail=cur
        cur.next=None
        
    def __str__(self):
        cur = self.head
        out = []
        while cur:
            out.append(cur.val)
            cur = cur.next
        return str(out)

que=Queue(4)
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
print(que)
que.rotate(2)
print(que)
print(que.head)
print(que.tail)
# que.dequeue()
# que.dequeue()
# que.dequeue()
# que.dequeue()
# print(que)