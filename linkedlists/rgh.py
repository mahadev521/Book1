f=head
s=head
count=1
while count<=n and f:
    f=f.next
    count+=1
while f and f.next:
    s=s.next
    f=f.next
if f:
    s.next=s.next.next
else:
    head=None