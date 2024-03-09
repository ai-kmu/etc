class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        answer, max_val = 0, 0
        # 왼쪽 값은 오름차순으로 정렬하고, 왼쪽 값이 같으면 오른쪽 값은 내림차순으로 정렬
        # 1. 왼쪽 값이 같은 경우 뒤쪽은 항상 왼쪽 값 안에 속하게 됨
        # 2. 왼쪽 값이 같은 경우 리스트를 순회할수록 왼쪽 값은 항상 앞쪽에 속하므로
        # 오른쪽 값이 기존 최댓값 안에만 속하는지만 확인하면 됨
        intervals.sort(key=lambda x: (x[0], -x[1]))
        for _, j in intervals:
            if j > max_val:
                answer += 1
                max_val = j
        return answer
        
