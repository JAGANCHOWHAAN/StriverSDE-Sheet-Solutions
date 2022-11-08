class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res1=Counter(s)
        res2=Counter(t)
        if res1==res2:
            return True
        return False
        