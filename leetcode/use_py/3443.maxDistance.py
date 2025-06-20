def maxDistance(self, s: str, k: int) -> int:
    ans,X,x,Y,y=0,0,0,0,0
    for i in range(len(s)):
        if s[i]=="N":
            Y+=1
        elif s[i]=="S":
            y+=1
        elif s[i]=="E":
            X+=1
        elif s[i]=="W":
            x+=1
        MD=abs(X-x)+abs(Y-y)
        dis=MD+min(k*2,i+1-MD)
        ans=max(ans,dis)
    return ans
