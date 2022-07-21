# # def fun(x,n):
# #     if n==0: return 1
# #     pro=1
# #     for i in range(abs(n)): pro*=x
# #     return 1/pro if n<0 else pro
# def fun(a, n):
#     ans = 1
#     while (n > 0):
#         last_bit = (n & 1)
#         # Check if current LSB
#         # is set
#         if (last_bit):
#             ans = ans * a
#         a = a * a
#         # Right shift
#         n = n >> 1
#     return ans

# print(fun(2,3))
# print(fun(2,-2))
# print(fun(2,0))
# print(pow(2,3))


def po(x,n):
    if n==0: 
        return 1
    if n<0:
        return 1/po(x,-n)
    prod= pow(x,n//2)
    return prod*prod*x if n%2!=0 else prod*prod
    
print(po(6,-5))
