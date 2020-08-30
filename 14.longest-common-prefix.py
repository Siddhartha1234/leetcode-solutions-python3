class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        comm = ""
        ind = 0
        
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        while True:
            if any([ind >= len(w) for w in strs]):        
                break
            
            if not all([w[ind] == strs[0][ind] for w in strs]):
                break
            
            comm += strs[0][ind]
            ind += 1
            
        return comm
