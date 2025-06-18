def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    Element=len(nums)
    Nnums=[]
    if (Element%3)==0:
        nums.sort()
        index,find=0,True
        while((index/3)<(Element/3) and find):
            if abs(nums[index]-nums[index+1])<=k and abs(nums[index+1]-nums[index+2])<=k and abs(nums[index]-nums[index+2])<=k:
                Nnums.append([nums[index],nums[index+1],nums[index+2]])
                index+=3
            else:
                find=False
                break
    if find==False:
        return []
    else:
        return Nnums