def fun(n,l):
    for i in range(n-1):
        if l[i]==l[i+1]:
            if i!=0:
                l[i]=(l[i-1]+l[i])/2
            else:
                return 'No'
            continue
        while l[i]>l[i+1]:
            l[i]=(l[i]+l[i+1])/2
            if l[i]==l[i+1]: return 'No'
    return 'Yes'
                           
    
n=int(input())
l=[int(x) for x in input().split()]
print(fun(n,l))