def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    Element=len(nums)
    Nnums=[]
    if (Element%3)==0:
        nums.sort()
        index=0
        while((index/3)<(Element/3)):
            if abs(nums[index]-nums[index+2])<=k:
                Nnums.append([nums[index],nums[index+1],nums[index+2]])
                index+=3
            else:
                return []
    return Nnums