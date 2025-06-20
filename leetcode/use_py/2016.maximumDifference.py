#maximumDifference
def maximumDifference(self, nums: List[int]) -> int:
    i,maxDif=1,0
    min_num=nums[0]
    while(i<len(nums)):
        if nums[i]<min_num:
            min_num=nums[i]
        else:
            Tmax=nums[i]-min_num
            if Tmax>maxDif:
                maxDif=Tmax
        i+=1
    if maxDif>0:
        return maxDif
    else:
        return -1