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