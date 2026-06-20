from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}

        for c in t:
            count[c] = count.get(c,0) + 1

        for c in s:
            if c not in count:
                return False
            
            count[c] -= 1
            if count[c]<0:
                return False
        return True


        


        