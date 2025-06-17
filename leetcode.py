#TwoSum
def twoSum(self, nums, target):
    lens=len(nums)
    for i in range(lens):
        for j in range(lens-(i+1)):
            a=nums[i]+nums[j+i+1]
            if a==target:
                return [i, j+i+1]
            else:
                continue