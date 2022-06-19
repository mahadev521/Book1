# l=input().split()
# for i in range(len(l)):
#     if i>len(l)//2-1:print(ord(l[i].lower())-1,end=' ')
#     else:
#         if l[i].isupper() : print(l[i].lower(),end=' ') 
#         else: print(l[i].upper(),end=' ')

l=input().split()
print(*l[1:]+[l[0]])