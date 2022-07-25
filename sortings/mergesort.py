def divide(arr,si,ei):
    if si>=ei: return
    mid= si + (ei-si)//2
    divide(arr,si,mid)
    divide(arr,mid+1,ei)
    conquer(arr,si,mid,ei)

def conquer(arr,si,mid,ei):
    left=arr[si:mid+1]
    right=arr[mid+1:ei+1]
    i,j,k=0,0,si
    # while i<=mid-si and j<=ei-mid-1:
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
    return arr

arr=[6,3,9,5,2,8]
divide(arr,0,len(arr)-1)
print(arr)