def issort(arr):
    return True if len(arr)==1 else arr[0]<=arr[1] and issort(arr[1:])
arr=[1,2,3,4,5]
print(issort(arr))
arr=[23,44,23,11,23,44]
print(issort(arr))