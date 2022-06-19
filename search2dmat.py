def fun(mat,target):
    
    def bin(lo,hi,arr):
        while lo<=hi:
            mid=(lo+hi)//2
            if arr[mid]==target: return True
            if arr[mid]>target: hi=mid-1
            if arr[mid]<target: lo=mid+1
        return False
    for i in mat:
        if target<=i[-1]:
            print(i)
            if i[0]==target or i[-1]==target: 
                return True
            return bin(0,len(mat[0]),i)
        
    
    # nums=[i[-1] for i in mat]
    # ind=bin(0,len(nums),nums)
    # print(ind)
    # if mat[ind][0]==target: return True
    # ind2=bin(0,len(mat[0]),mat[ind])
    # return mat[ind][ind2]==target



mat=[[1,7,11,15],
     [17,20,27,29],
     [34,38,39,41],
     [44,56,77,89]]
print(fun(mat,20))



# def fun2(n):
#     def fun(n):
#         if n%2==0: return True
#         return False
#     return fun(n)

# print(fun2(34))
