class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        cols = max([len(x) for x in words])
        cols = ["" for _ in range(cols)]
        for word in words:
            j = 0
            for i in range(len(cols)):
                if j >= len(word): cols[i] += ' '
                else: cols[i] += word[j]
                j += 1
        for i in range(len(cols)):
            col = cols[i]
            if not col.endswith(' '): continue
            cols[i] = col.rstrip()

        return cols
