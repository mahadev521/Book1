class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None

    def __str__(self):
        return f'{self.val},{self.next}'
    
class CLL:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.head.next = self.head
            return
        cur=dum=self.head
        while cur.next is not dum:
            cur=cur.next
        cur.next=Node(val)
        cur.next.next=dum
            
    def display(self,head):
        cur=self.head
        op = [str(cur.val)]
        cur=cur.next
        while cur is not self.head:
            op.append(str(cur.val))
            cur=cur.next
        return ' -> '.join(op)

    def splitl(self,head):
        f=s=head
        while f.next is not head and f.next.next is not head:
            f=f.next.next
            s=s.next
        print(f'second half is {self.display(s.next)}')

cll=CLL()
cll.insert(1)
cll.insert(2)
cll.insert(3)
cll.insert(4)
print(cll.display(cll.head))
cll.splitl(cll.head)
