from collections import Counter
def fun(nums):
    n=len(nums)
    nums=Counter(nums).most_common(1)[0]
    print(nums)
    if nums[1]>n//2:
        return nums[0]

nums=[2,3,3,3,3,2,2,2]
print(fun(nums))