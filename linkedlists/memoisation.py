def fun(n,memo):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fun(n-1,memo) + fun(n-2,memo)
    return memo[n]

n=7
memo={}
print(fun(n,memo))