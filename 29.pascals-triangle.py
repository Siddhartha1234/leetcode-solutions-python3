class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        cnt = numRows
        l = [[1], [1, 1]]
        while cnt > 1:
            nl = [1]
            for i in range(len(l[-1]) - 1):
                nl.append(l[-1][i] + l[-1][i + 1])
            nl += [1]
            l.append(nl)
            cnt -= 1

        return l[:numRows]
