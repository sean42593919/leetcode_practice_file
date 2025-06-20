def romanToInt(self, s: str) -> int:
    Roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    Sum=[]
    i=0
    while(i<len(s)):
        if i+1<len(s):
            if Roman[s[i]]<Roman[s[i+1]]:
                Sum.append(Roman[s[i+1]]-Roman[s[i]])
                i+=2
            else:
                Sum.append(Roman[s[i]])
                i+=1
        else:
            Sum.append(Roman[s[i]])
            i+=1
    ans=sum(Sum)    
    return ans