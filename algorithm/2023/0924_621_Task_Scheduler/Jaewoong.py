# 풀이 실패해서 정답보고 공부했습니다
# 리뷰안해주셔도되요
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 알파벳 개수(대문자로 가정)만큼의 배열 초기화
        task_counts = [0] * 26  
        for task in tasks:
            # 작업 빈도수 증가
            task_counts[ord(task) - ord('A')] += 1  
        
        # 빈도수에 따라 내림차순으로 정렬
        task_counts.sort(reverse=True)  
        # 가장 빈도가 높은 작업의 빈도수
        max_count = task_counts[0]  

        # 가장 빈도가 높은 작업을 수행하고, 그 사이에 다른 작업들을 삽입
        idle_time = (max_count - 1) * n
        for i in range(1, len(task_counts)):
            idle_time -= min(max_count - 1, task_counts[i])
            print(idle_time)
        # idle_time이 음수가 되지 않도록 보정
        idle_time = max(0, idle_time)  
        # 총 시간은 작업 수와 대기 시간의 합
        return len(tasks) + idle_time          
