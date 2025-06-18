def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    Nnums=[]
    if (len(nums)%3)==0:
        nums.sort()
        for index in range(len(nums)/3):
            if nums[(index*3)+2]-nums[(index*3)]<=k:
                Nnums.append(nums[(index*3):(index*3)+3])
            else:
                return []
    return Nnums