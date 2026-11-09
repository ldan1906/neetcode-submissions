class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): 
            return False
        checks = {}
        for i in range(len(s)): 
            checks[s[i]] = checks.get(s[i],0) + 1
        checkt = {}
        for i in range(len(t)): 
            checkt[t[i]] = checkt.get(t[i],0) + 1

        return checks == checkt  

            

                