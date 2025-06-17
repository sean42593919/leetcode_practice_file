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
#lengthOfLongestSubstring
def lengthOfLongestSubstring(self, s: str) -> int:
    characters=[]
    hashmap={}
    strlens=len(s)
    for i in range(strlens):
        for j in range(i,strlens):
            if s[j] in characters:
                hashmap[i]=characters
                characters=[]
                break
            else:
                characters.append(s[j])
                if len(characters)==strlens:
                    hashmap[0]=characters
                    characters=[]
    if strlens==0:
        longest_len=0
    else:
        MAX_value=max(hashmap.values(),key=len)
        longest_len=int(len(MAX_value))
    return longest_len
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
#minMaxDifference
def minMaxDifference(self, num: int) -> int:
    Digit=int(len(str(abs(num))))
    nums=num
    for i in range(Digit,0,-1): 
        digits=abs(nums)//(10**(i-1))
        print(digits)
        if digits!=9:
            break
        nums-=9*(10**(i-1))
    MD=abs(num)//(10**(Digit-1))
    MAX_num=int(str(num).replace(str(digits),'9'))
    MIN_num=int(str(num).replace(str(MD),'0'))
    NEW_num=abs(MAX_num-MIN_num)
    return NEW_num
#longestPalindrome
def longestPalindrome(self, s: str) -> str:
    strlen=len(s)
    Pallist=[]
    for i in range(1,strlen-1):
        counter=1
        find=True
        while(find):#odd
            if s[i+counter]==s[i-counter]:
                counter+=1
                if ((i+counter)>=strlen) or ((i-counter)<0):
                    counter-=1
                    Pallist.append(s[i-counter:i+counter+1])
                    find=False
            else:
                counter-=1
                Pallist.append(s[i-counter:i+counter+1])
                break
        counter=0
        find=True
        while(find):#even
            if s[i+counter]==s[i-counter-1]:
                counter+=1
                if ((i+counter)>=strlen) or ((i-counter-1)<0):
                    counter-=1
                    Pallist.append(s[i-counter-1:i+counter+1])
                    find=False
            else:
                counter-=1
                Pallist.append(s[i-counter-1:i+counter+1])
                break
        if i==strlen-2:
            if s[i]==s[i+1]:
                Pallist.append(s[i:i+2])
    if strlen==1:
        return s
    elif strlen==2:
        if s[0]==s[1]:
            return s
        else:
            return s[0]
    else: 
        return max(Pallist,key=len)