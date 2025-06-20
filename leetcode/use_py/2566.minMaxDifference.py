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