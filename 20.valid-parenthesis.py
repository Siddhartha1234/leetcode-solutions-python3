class Solution:
    def isValid(self, s: str) -> bool:
        opp = {'(': ')', '{': '}', '[': ']'}
        st = []
        for x in s:
            if len(st) == 0:
                if x in opp.values():
                    return False
                else:
                    st.append(x)
            elif x in opp.values():    
                if x == opp[st[-1]]:
                    st.pop()
                else:
                    return False
            else:
                st.append(x)
                
        return len(st) == 0
