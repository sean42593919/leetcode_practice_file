def partitionArray(self, nums: List[int], k: int) -> int:#without changing the order of the list but Time Complexity is O(n^2) so Time Limit Exceeded(NOT True ans in leetcode)
    Nnums=[]
    while(nums):
        Tnums=[]
        Tnums.append(nums.pop(nums.index(min(nums))))
        num=len(nums)
        count=0
        for i in range(num):
            if nums[count]-min(Tnums)<=k:
                Tnums.append(nums.pop(count))
            else:
                count+=1
        Nnums.append(Tnums)
    return len(Nnums)

def partitionArray(self, nums: List[int], k: int) -> int:#True ans in leetcode
    nums.sort()
    Nnums,Tnums=[],[]
    Tnums.append(nums.pop(0))
    for i in range(len(nums)):
        if nums[i]-Tnums[0]<=k:
            Tnums.append(nums[i])
        else:
            Nnums.append(Tnums)
            Tnums=[]
            Tnums.append(nums[i])
    if Tnums:
        Nnums.append(Tnums)
    return len(Nnums)