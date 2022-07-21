def canSum(head):
    f=s=head
    prev=None
    while f and f.next:
        f=f.next.next
        prev=s
        s=s.next
    prev.next=None
    f=head
    dosum(f,s)
    # dum=None
    # print(f,s,sep='\n')
    # #for carry
    # c=0
    # while f and s:
    #     x=f.data+s.data+c
    #     if x>9:
    #         c=x//10
    #         x=x%10
    #     else:c=0
    #     # always inserting in front
    #     temp=Node(x)
    #     temp.next=dum   
    #     dum=temp
    #     f=f.next
    #     s=s.next
    # print(temp)
        
def dosum(heada,headb):
    cur=heada
    lena=1
    lenb=1
    while cur:
        cur=cur.next
        lena+=1
    cur=headb
    while cur:
        cur=cur.next
        lenb+=1
    if lenb<lena:
        for _ in range(lena-lenb):
            temp=Node(0)
            temp.next=headb
            headb=temp
    elif lenb>lena:
        for _ in range(lenb-lena):
            temp=Node(0)
            temp.next=heada
            heada=temp
    dum=None
    while heada and headb:
        x=heada.data+headb.data
        temp=Node(x)
        temp.next=dum   
        dum=temp
        heada=heada.next
        headb=headb.next
    print(temp)
    cur=temp
    carry=0
    while cur.next:
        x=cur.data+carry
        if x>9:
            cur.data=x%10
            carry=x//10
        cur=cur.next
    x=cur.data+carry
    if x>9:
        cur.data=x%10
        carry=x//10
        cur.next=Node(carry)
    else:
        cur.data=x
    print(temp)
    

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
def rem_dups(head):
    '''TC:O(n) & SC=O(n)'''
    # cache=set()
    # prev=None
    # cur=head
    # while cur:
    #     if cur.data in cache:
    #         prev.next=cur.next
    #     else:
    #         cache.add(cur.data)
    #         prev=cur
    #     cur=cur.next
    # return head
    '''TC:O(n^2) & SC=O(1)'''
    cur=head
    while cur:
        run=cur
        while run.next:
            if run.next.data==cur.data:
                run.next=run.next.next
            else:
                run=run.next
        cur=cur.next
    return head

def kthlast(head,k):
    k=1 if k==0 else k
    f=s=head
    for _ in range(k):
        if not f: return None
        f=f.next
    while f:
        f=f.next
        s=s.next
    return s.data

def removeMid(head):
    dum=Node(0,head)
    dum.next=head
    f=head
    s=dum
    while f and f.next:
        f=f.next.next
        s=s.next
    s.next=s.next.next
    return head

def partition(node,x):  # sourcery skip: avoid-builtin-shadow
    head=tail=node
    while node!=None:
        next=node.next
        if node.data<x:
            node.next=head
            head=node
        else:
            tail.next=node
            tail=node
        node=next
    tail.next=None
    return head
    # 1 -> 2 -> 3 -> 5 -> 8 -> 5 -> 10 -> None


def reverse(head):  # sourcery skip: avoid-builtin-shadow
    cur=head
    prev=None
    while cur:
        next=cur.next
        cur.next=prev
        prev=cur
        cur=next
    return prev


'''input for intersecting links'''
# ll=SLL()
# ll.extend([11,12,1,2,3,4,5])
# ll1=SLL()
# ll1.extend([10,20])
# cur=ll.head
# for _ in range(2):
#     cur=cur.next
# cr=ll1.head
# while cr.next:
#     cr=cr.next
# cr.next=cur
# print(ll.head)
# print(ll1.head)


# ll.extend([1,2,1,3,2,4,5,6,5])
#midele
# ll.extend([1,2,3,4,5,6,7])
# print(removeMid(ll.head))
#partition
# ll.extend([3,5,8,5,10,2,1])



# ll=SLL()
# ll.extend([6,1,7,2,9,5])
# ll.head=reverse(ll.head)
# print(canSum(ll.head))


# print(partition(ll.head,5))
# print(rem_dups(ll.head))
# print(kthlast(ll.head,12))
