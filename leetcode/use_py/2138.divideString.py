def divideString(self, s: str, k: int, fill: str) -> List[str]:
    unfill=k-(len(s)%k)
    while(k>unfill>0):
        s=s+fill
        unfill-=1
    ans=[]
    for i in range(len(s)//k):
        ans.append(s[i*k:(i+1)*k])
    return ans