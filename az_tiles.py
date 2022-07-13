def fun(n):
    if n<=0: return 0
    memo=[1,2,3]+[0]*(n-3)
    for i in range(3,n):
        memo[i]=memo[i-1]+memo[i-2]
    return memo[n-1]%1000000007
n=int(input())
print(fun(n))