'''singly linked list'''

from errno import E2BIG


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self,val):
        self.iend(val)

    def extend(self,arr):
        # extending the singly linked list
        cur= self.head
        if cur==None:
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
        if self.head == None:
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
        if self.head==None:
            print('there is no head')
            return
        else:
            self.head=self.head.next
            self.length-=1
    
    # delete element at the tail
    def deltail(self):
        if self.head==None:
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
    def delele(self,val):
        pos=self.getPos(val)
        if pos!=-1:
            self.delatpos(pos)
        else:
            print('element doesn\'t exist')
    
    # get posotion of an element in the linked list
    def getPos(self,val):
        pos=1
        cur = self.head
        while cur:
            if cur.data==val:
                return pos
            cur = cur.next
            pos+=1
        return -1
    
    # get value/ data at a position
    def getVal(self,pos):
        count=1
        cur = self.head
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
    
    def reverse(self):
        # reversing the singly linked list
        # print(self.length)
        # for i in range(self.length//2):
        #     self.swap(i+1,self.length-i)

        # prev = None
        # curr = self.head
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # self.head = prev
        prev=None
        cur=self.head
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        self.head = prev
        
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

ll=SLL()
ll.extend([1,2])
print(ll)
ll.delNthFromLast(2)
print(ll)




# ll.extend([23,45,47,22,56,78,23,98,45,76,99])
# print(ll)
# ll.delNthFromLast(3)
# print(ll)
# ll.append(12)
# ll.extend([23,45,66,76,87,98,109,120])
# print(ll.isPalindrome())
# print(ll)
# ll.reverse()
# print(ll)
# print(ll.getPos(66))
# print(ll.length)




# ll.append(23)
# ll.append(29)
# ll.append(43)
# ll.append(34)
# ll.append(67)
# ll.append(77)
# ll.append(97)
# ll.append(82)
# print(ll)
# ll.updatePosition(3,99)
# print(ll)
# ll.swapnodes(12,67)
# print(ll)



# ll.ibegin(45)
# ll.iend(77)
# ll.iatpos(34,2)
# print(ll)
# print(ll.length)
# ll.delhead()
# # ll.deltail()
# # ll.delatpos(1)

# # print(ll.getPos(34))
# # ll.delele(34)
# # ll.reverse()
# print(ll)


