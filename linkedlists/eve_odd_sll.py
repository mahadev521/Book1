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

def fun(head):
    newh=newt=None
    newsh=newst=None
    itr=head
    while itr:
        # print(itr)
        if itr.data%2==0:
            # this is because the next pointer may be odd and still consider it to be even vice versa
            if newst and newst.next==itr:
                newst.next=None
            #keep the head constant (good practice)
            if newh is None:
                newh=newt=itr
            #always update the tail 
            else:
                newt.next=itr
                newt=newt.next
        else:
            if newt and newt.next==itr:
                newt.next=None
            if newsh is None:
                newsh=newst=itr
            else:
                newst.next=itr
                newst=newst.next
        itr=itr.next
        
    #if we need even before odd
    # if newh is None:
    #     return newsh
    # newt.next=newsh
    # return newh

    #if we need odd before even
    if newsh is None:
        return newh
    newst.next=newh
    return newsh

    '''using extra space for new pointers'''
    # newh=newt=None
    # newsh=newst=None
    # itr=head
    # while itr:
    #     # print(itr)
    #     if itr.data%2==0:
    #         if newh is None:
    #             newh=newt=Node(itr.data)
    #         else:
    #             newt.next=Node(itr.data)
    #             newt=newt.next
    #     elif newsh is None:
    #         newsh=newst=Node(itr.data)
    #     else:
    #         newst.next=Node(itr.data)
    #         newst=newst.next
    #     itr=itr.next
    # if newh is None:
    #     return newsh
    # newt.next=newsh
    # return newh
        
ll=SLL()
ll.extend([1,2,3,4,5,6,7,8,9,10,11])
# ll.extend([1,3,5,7,9,11])
# ll.extend([2,4,6,8,10])
print(fun(ll.head))