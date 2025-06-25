def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
    num=[]
    aindex=set()
    for i in range(len(nums)):
        if nums[i]==key:
            num.append(i)
    for i in range(len(num)):
        start=max(0,num[i]-k)
        end=min(len(nums),num[i]+k+1)
        aindex.update(range(start,end))
    return sorted(list(aindex))