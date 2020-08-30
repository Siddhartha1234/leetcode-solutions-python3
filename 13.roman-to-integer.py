class Solution:
    def romanToInt(self, s: str) -> int:
        val = { 'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        res = 0
        ind = 0
        while ind < len(s):
            if ind < len(s) - 1 and val[s[ind]] < val[s[ind + 1]]:
                res += ( - val[s[ind]] + val[s[ind + 1]] )
                ind += 2
            else:
                res += val[s[ind]]
                ind += 1
        
        return res
