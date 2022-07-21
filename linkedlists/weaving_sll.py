class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f'{self.data} -> {self.next}'
    
class SLL:
    def __init__(self):
        self.head = None
        self.length = 0


    def extend(self,arr):
        # extending the singly linked list
        cur= self.head
        if cur is None:
            self.head=Node(arr[0])
            cur=self.head
            if len(arr)>1:
                for i in arr[1:]: 
                    self.length +=1
                    cur.next=Node(i)
                    cur=cur.next
            self.length +=1
        else:
            while cur.next: 
                cur=cur.next
            for i in arr: 
                self.length +=1
                cur.next=Node(i)
                cur=cur.next

def weave(heada,headb):  # sourcery skip: avoid-builtin-shadow
    f=heada
    s=headb
    prev=None
    print(f,'first')
    while f and s:
        next=f.next
        snext=s.next
        f.next=s
        f.next.next=next
        prev=f.next
        f=next
        s=snext
    if f:
        prev.next=f
    if s:
        prev.next=s
    return heada

def splits(head):
    f=s=head
    prev=None
    while f and f.next:
        f=f.next.next
        prev=s
        s=s.next
    f=head
    prev.next=None
    return weave(f,s)
    
# oddnum=SLL()
# oddnum.extend([1,3,5])
# evennum=SLL()
# evennum.extend([2,4,6,8,10])
# print(weave(oddnum.head,evennum.head))

split=SLL()
split.extend([1,2,3,4,5,6,7,8,9])
f=splits(split.head)
print(f)