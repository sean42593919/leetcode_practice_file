import heapq
def Baseconversion(k,n):
    k_num=""
    while(n!=0):
        k_num+=str(n%k)
        n//=k
    return k_num[::-1]

def generate_odd():
    half=1
    while True:
        s=str(half)
        yield int(s+s[:-1][::-1])
        half+=1

def generate_even():
    half=1
    while True:
        s=str(half)
        yield int(s+s[::-1])
        half+=1

def kMirror(self, k: int, n: int) -> int:
    nums=[]
    count=0
    p=heapq.merge(generate_odd(),generate_even())
    while(len(nums)<n):
        num=next(p)
        K_num=Baseconversion(k,num)
        if K_num==K_num[::-1]:
            nums.append(num)
        count+=1    
    ans=sum(nums)
    return ans