class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        cnt = 1
        l = [1, 1]
        nxt = [1, 1]
        while cnt != rowIndex:
            l = nxt
            nl = [1]
            for i in range(len(l) - 1):
                nl.append(l[i] + l[i + 1])
            nl += [1]
            nxt = nl
            cnt += 1

        return nxt
