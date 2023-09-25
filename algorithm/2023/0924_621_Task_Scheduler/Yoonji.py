class Solution:
    def leastInterval(self, tasks, n):
        # n을 주기당 최대 수행할 수 있는 작업 수로 재정의
        n += 1
        # 작업을 빈도수를 세는 딕셔너리로 수집
        dic = {}
        for x in tasks:
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1
        
        # 가장 큰 병목 현상을 가진 작업의 빈도수
        bneck = 0
        # 위 빈도수를 가진 작업의 개수
        bnecks = 1
        for x in dic.values():
            if x > bneck:
                bneck = x
                bnecks = 1
            elif x == bneck:
                bnecks += 1
        
        # 최소 실행 시간을 계산하여 반환
        return max(len(tasks), n * (bneck - 1) + bnecks)
