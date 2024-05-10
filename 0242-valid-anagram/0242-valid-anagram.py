class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash = {} 
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1

        for j in t:
            if j in hash:
                hash[j] -= 1
            else:
                return False
                
            
        for x in hash:
            if hash[x] != 0:
                return False
            return True

    