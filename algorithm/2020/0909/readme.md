https://leetcode.com/problems/merge-intervals/

```{.python}
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):      # 간격의 앞 기준으로 오름차순 정렬
            if out and i[0] <= out[-1][1]:                   # 간격이 겹치는 경우
                out[-1][1] = max(out[-1][1], i[1])           # 최근 간격의 뒤 = 대상 간격, 최근 간격 중 더 넓은 범위로 확장
            else:
                out += i,
        return out
```
