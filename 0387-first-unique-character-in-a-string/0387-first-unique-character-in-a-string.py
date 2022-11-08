class Solution:
    def firstUniqChar(self, s: str) -> int:
        res={}
        for i in range(len(s)):
            if s[i] not in res:
                res[s[i]]=1 
            else:
                res[s[i]]+=1 
        for i in range(len(s)):
            if res[s[i]]==1:
                return i
        return -1