class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
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

def add(heada,headb):
    l1=l2=0
    cur=heada
    while cur:
        cur=cur.next
        l1+=1
    cur=headb
    while cur:
        cur=cur.next
        l2+=1
    if l1>l2:
        for _ in range(l1-l2):
            temp=Node(0)
            temp.next=headb
            headb=temp
    elif l2>l1:
        for _ in range(l2-l1):
            temp=Node(0)
            temp.next=heada
            heada=temp
    added= sums(heada,headb)
    if not added.data:
        return added.next
    return added

def sums(heada,headb):
    #base case
    if heada is None and headb is None:
        return Node(0)
    temp=sums(heada.next,headb.next)
    x=heada.data+headb.data+temp.data
    #check if it has carry
    carry=x//10
    val=x%10
    # update currents node data if its greater than 9
    temp.data=val
    return Node(carry,temp)
    

ll1=SLL()
# ll1.extend([1,2,3])
ll1.extend([7,9,0,1])

ll2=SLL()
# ll2.extend([1,2,3])
ll2.extend([1,0,0,7])

print(ll1.head,ll2.head)
print(add(ll1.head,ll2.head))