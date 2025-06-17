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
#addTwoNumbers
#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def get_length(node):
        length=0
        while node:
            length+=1
            node=node.next
        return length
    l3=ListNode()
    carry=0
    node=l3
    l1_len=get_length(l1)
    l2_len=get_length(l2)
    for i in range(l1_len if l1_len>l2_len else l2_len):
        l1num=l1.val if l1 else 0
        l2num=l2.val if l2 else 0
        l3num=l1num+l2num+carry
        carry=0
        if l3num>9:
            l3num-=10
            carry=1
        node.next=ListNode(l3num)
        l1=l1.next if l1 else 0
        l2=l2.next if l2 else 0
        node=node.next
    if carry==1:
        node.next=ListNode(1)
    return l3.next
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
        while(True):
            if s[i+counter]==s[i-counter]:
                counter+=1
            else:
                counter-=1
                Pallist.append(s[i+counter:i-counter])
                find=True
            if find==True:
                break
    if Pallist==None:
        return s[0]
    else: return max(Pallist,key=len)

s="ababd"