class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=ransomNote
        m=magazine
        m_l=list(m)
        for ch in r:
            if ch in m_l:
                m_l.remove(ch)
            else:
                return 0
        return 1