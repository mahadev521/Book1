'''singly linked list'''

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

    def append(self,val):
        self.iend(val)

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
     
    # insert at beginning
    def ibegin(self, node):
        self.length += 1
        node= Node(node)
        node.next = self.head
        self.head = node
    
    #insert at end
    def iend(self, node):
        self.length += 1
        node = Node(node)
        if self.head is None:
            self.head = node
            return
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    #insert at position
    def iatpos(self, node, pos):
        if pos > self.length+1:
            print('insertion not possible')
            return
        if pos == 1:
            self.ibegin(node)
            return
        elif pos == self.length+1:
            self.iend(node)
            return
        cur = self.head
        count = 1
        while cur.next:
            count += 1
            if count == pos:
                self.length += 1
                node = Node(node)
                node.next, cur.next = cur.next, node
                return
            cur = cur.next

    #delete element at the head
    def delhead(self):
        if self.head is None:
            print('there is no head')
            return
        else:
            self.head=self.head.next
            self.length-=1
    
    # delete element at the tail
    def deltail(self):
        if self.head is None:
            print('there is no tail')
            return
        else:
            cur=self.head
            while cur.next.next:
                cur=cur.next
            cur.next=None
            self.length-=1
            
    # delete element at the specified position    
    def delatpos(self, pos):
        if pos > self.length+1:
            print('deletion not possible')
            return
        if pos == 1:
            self.delhead()
            return
        elif pos == self.length+1:
            self.deltail()
            return
        cur = self.head
        count = 1
        while cur.next:
            count += 1
            if count == pos:
                self.length -= 1
                cur.next=cur.next.next
                return
            cur = cur.next

    #delete an element by value
    def delete(self,val):
        cur=self.head
        if cur.data==val:
            self.head=cur.next
            return
        while cur.next.data!=val and cur.next.next:
            cur=cur.next
        cur.next=cur.next.next
    
    # get posotion of an element in the linked list
    def getPos(self,val):
        pos=1
        cur = self.head
        while cur and cur.data!=val:
            cur = cur.next
            pos+=1
        return pos if cur else -1
    
    # get value/ data at a position
    def getVal(self,pos):
        cur = self.head
        # while pos>1:
        #     cur=cur.next
        #     if not cur: return -1
        #     pos-=1
        # return cur.data or -1
        count=1
        while cur:
            if count==pos:
                return cur.data
            cur = cur.next
            count+=1
        return -1
    # for updating a positions value
    def updatePosition(self,pos,val):
        cur=self.head
        count=1
        while cur:
            if count==pos:
                cur.data=val
                return
            count+=1
            cur=cur.next
    
    #swap based on values
    def swapnodes(self,val1,val2):
        pos1= self.getPos(val1)
        pos2= self.getPos(val2)
        self.updatePosition(pos1,val2)
        self.updatePosition(pos2,val1)
    
    # based on index    
    def swap(self,pos1,pos2):    
        val1=self.getVal(pos1)
        val2=self.getVal(pos2)
        # print(val1,val2)
        # print(pos1,pos2)
        self.updatePosition(pos1,val2)
        self.updatePosition(pos2,val1)
    #display
    def __str__(self):
        s = []
        curr_node = self.head
        while curr_node:
            s.append(str(curr_node.data))
            curr_node = curr_node.next
        return ' -> '.join(s)
        # return ' -> '.join(s[::-1]) #reverse printing
    #get head value         
    def gethead(self):
        return self.head.data
    
    # def reverse(self):
        # prev=None
        # cur=self.head
        # while cur:
        #     nxt=cur.next
        #     cur.next=prev
        #     prev=cur
        #     cur=nxt
        # self.head = prev
        
    def isPalindrome(self):
        rec=[]
        cur=self.head
        while cur:
            rec.append(cur.data)
            cur=cur.next
        cur=self.head
        for i in rec[::-1]:
            if i!=cur.data:
                return False
            cur=cur.next
        return True
    
    #using fast and slow algorithm
    def delNthFromLast(self,n):
        f=s=self.head
        for _ in range(n):
            f=f.next
        if not f:
            self.head=self.head.next
            return
        while f.next:
            f=f.next
            s=s.next
        s.next=s.next.next
# list1=Slist1()
# list1.extend([1,2])
# print(list1)
# list1.delNthFromLast(2)
# print(list1)

def reverse(head):
    if head is None or head.next is None:
        return head
    rl=reverse(head.next)
    head.next.next=head
    head.next=None
    return rl

def rotate(head,k):
    # if k==0: return head
    # temp=head
    # f,s=head,head
    # for _ in range(k):
    #     f=f.next
    # while f:
    #     s=s.next
    #     f=f.next
    # head=s
    # print(s,temp,head)
    if not k or not head or not head.next:
        return head
    cur=head
    size=1
    while cur.next:
        size+=1
        cur=cur.next
    cur.next=head
    k=k%size
    k=size-k
    while k:
        cur=cur.next
        k-=1
    head=cur.next
    cur.next=None
    return head
    
def merge(a,b):
    if not a or b and a.data > b.data:a, b = b, a
    if a: a.next = merge(a.next, b)
    return a

#recursively print elements from enting node
def printRev(head):
    if not head: return head
    printRev(head.next)
    print(head.data)

def lenEven(head):
    try:
        while head:
            head=head.next.next
        return 'even'
    except Exception:
        return 'odd'
    
def merges(heada,headb):
    '''3rd variable'''
    # headc=Node()
    # temp=headc
    # while heada and headb:
    #     if heada.data < headb.data:
    #         headc.next=heada
    #         heada=heada.next
    #     else:
    #         headc.next=headb
    #         headb=headb.next
    #     headc=headc.next
    # headc.next=heada or headb
    # return temp.next
    
    
    temp=heada
    while heada and headb:
        if heada.data < headb.data:
            print(heada.data,headb.data)
            heada=heada.next
        else:
            heada=Node(999)
            heada.next=None
            break
    print(temp)
    print(heada)
    # print(heada)
    # while heada and headb:
    #     # print(heada)
    #     temp=heada
    #     if heada.data<headb.data:
    #         heada=heada.next
        # else:
        #     nxt=heada.next
        #     heada.next=headb
        #     heada.next.next=nxt
            # # node=headb
            # node.next=heada
    # print(temp)
    # heada.next= heada or headb
    # return heada
    
'''swapping pairs'''
def swapPairs(head):
    '''iterative'''
    # dum=p=Node(0)
    # dum.next=head
    # while head and head.next:
    #     temp=head.next
    #     head.next=head.next.next
    #     temp.next=head
    #     head=head.next
    #     p.next=temp
    #     p=temp.next
    # print(dum.next)
    
    if head and head.next:
        temp=head.next
        head.next=swapPairs(temp.next)
        temp.next=head
        return temp
    return head

    # if head and head.next:
    #     tmp = head.next
    #     head.next = swapPairs(tmp.next)
    #     tmp.next = head
    #     return tmp
    # return head

def revKnodes(head,k):
    #base case
    ptr=head
    for _ in range(k):
        if ptr is None: return head
        ptr=ptr.next
    #snippet for reversing k nodes
    cur=None
    ptr=head
    for _ in range(k):
        nxt=ptr.next
        ptr.next=cur
        cur=ptr
        ptr=nxt
    # recursive call
    head.next=revKnodes(ptr,k)
    return cur


ll=SLL()
ll.extend([1,2,5,6,7,8])
# print(swapPairs(ll.head))
print(revKnodes(ll.head,4))
# ll.extend([1,2,4,7,9,11,16,23])
# ll2=SLL()
# ll2.extend([3])
# ll2.extend([3,6,8,12,15,27,33,45])
# print(merges(ll.head, ll2.head))

# x=reverse(ll.head)
# printRev(ll.head)
# print(lenEven(ll.head))

# x=rotate(ll.head,3)
# print(ll)

# v=ll.getVal(0)
# print(v)
# print(ll.getPos(v))


'''merging two sorted linked lists'''
# list1=Slist1()
# # list1.extend([])
# list2=Slist1()
# list2.extend([2,4,6,7,22,45,78,82,90,94,101])
# print(merge(list1.head,list2.head))
# list1.extend([23,45,47,22,56,78,23,98,45,76,99])
# print(list1)
# list1.delNthFromLast(3)
# print(list1)
# list1.append(12)
# list1.extend([23,45,66,76,87,98,109,120])
# print(list1.isPalindrome())
# print(list1)
# list1.reverse()
# print(list1)
# print(list1.getPos(66))
# print(list1.length)


# list1.append(23)
# list1.append(29)
# list1.append(43)
# list1.append(34)
# list1.append(67)
# list1.append(77)
# list1.append(97)
# list1.append(82)
# print(list1)
# list1.updatePosition(3,99)
# print(list1)
# list1.swapnodes(12,67)
# print(list1)

# list1.ibegin(45)
# list1.iend(77)
# list1.iatpos(34,2)
# print(list1)
# print(list1.length)
# list1.delhead()
# # list1.deltail()
# # list1.delatpos(1)
# # print(list1.getPos(34))
# # list1.delele(34)
# # list1.reverse()
# print(list1)