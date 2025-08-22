class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []

        for c in operations:
            if c == '+':
                records.append(sum(records[-2:]))
            elif c == 'D':
                records.append(2 * records[-1])
            elif c == 'C':
                records.pop()
            else:
                records.append(int(c))

        return sum(records)
