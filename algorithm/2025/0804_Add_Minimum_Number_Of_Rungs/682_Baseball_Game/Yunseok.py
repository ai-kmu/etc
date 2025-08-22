from typing import List
"""
- For operation "+", there will always be at least two previous scores on the record.
- For operations "C" and "D", there will always be at least one previous score on the record.
"""

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        pointList = []
        for operation in operations:
            if operation == '+':
                pointList.append(pointList[-1] + pointList[-2])
            elif operation == 'D':
                pointList.append(pointList[-1] * 2)
            elif operation == 'C':
                pointList.pop()
            else:
                pointList.append(int(operation))
        
        return sum(pointList)
