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