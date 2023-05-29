# 풀이 실패...
# 리스트를 사용해서 노드에서 다음 노드로 갈때 몇개가 나가고, 연속된 나가는 노드에 따라서 최대값을 구하려고했는데 실패했습니다....
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dp_out = [0 for _ in range(n+1)]
        dp_in = [0 for _ in range(n+1)]
        for i in times:
            if i[1] - i[0] < 0:
                dp_in[i[1]] += 1
            if i[1] - i[0] > 0:
                dp_out[i[1]] += 1
        now = 0
        max_list = []
        for a in dp_in:
            now += 1
            max_list.append(now)
            if a == 0:
                now = 0
        return(max(max_list))

        
