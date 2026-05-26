class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = {}

        for ch in s:
            if ch not in sDict:
                sDict[ch] = 1
            else:
                sDict[ch] += 1

        for ch in t:
            if ch not in sDict or sDict[ch] == 0:
                return False
            
            sDict[ch] -= 1

        return True

        
        
        