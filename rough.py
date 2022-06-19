# from random import randint
# for i in range(10):
#     print(randint(1,99),end=',')

# arr=[2,-3,-6,-75,45,-67,-34,22,45,75,68,56,-45,-45,345,64,-3,56,6547,86,334]
# sig=1
# sig*=-1 for i in arr if i<0
# print(sig)

# arr1=[88,40,53,92,28,43,96,18,48,23]
# arr2=[64,40,74,67,61,20,22]
# # for i,j in zip(arr1, arr2):
# #     print(i,j)

# # arr1.sort()
# # for i,j in zip(arr1[:-1],arr1[1:]):
# #     print(i,j)

# x=98
# y=divmod(98,10)
# print(y)

# from collections import Counter
# s='bank'
# t='kanb'
# s=Counter(s)
# t=Counter(t)
# s=s-t
# print(s)


'''3'''
# def bitStrings(n):
#     if n == 0: return []
#     if n == 1: return ["0", "1"]
#     return [ digit+bitstring for digit in bitStrings(1) for bitstring in bitStrings(n-1)]

# print (bitStrings(2))

'''4'''
# def rangeToList(k):
#     result=[]
#     for i in range(0,k):
#         result.append(str(i))
#     return result

# def baseKStrings(n,k):
#     if n==0: return []
#     if n==1: return rangeToList(k)
#     return [digit+bitstring for digit in baseKStrings(1,k) for bitstring in baseKStrings(n-1,k)]

# print(baseKStrings(4,3))

'''cone area'''
# import sys
# from math import pi
# r=int(sys.stdin.readline().strip())
# h=int(sys.stdin.readline().strip())
# area=(pi*r*r*h)/3
# sys.stdout.write(str(round(area,3)))

'''scores'''
# import sys
# s=0
# for i in range(3):
#     s+=int(sys.stdin.readline().strip())*(3-i)
# for i in range(3):
#     s-=int(sys.stdin.readline().strip())*(3-i)
# if s>0:
#     print("Apples")
# elif s<0:
#     print("bananas")
# else:
#     print('TIE')