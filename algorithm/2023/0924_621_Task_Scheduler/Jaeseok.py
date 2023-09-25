from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        answer = 0
        # task_count는 각 task가 얼마나 남았는지를 셈
        task_count = Counter(tasks)
        
        # 모든 task를 다 수행할 때까지 반복
        while task_count:
            cycle = 0
            # task를 남은 개수로 정렬해서 가장 많이 남은 task부터 제거할 수 있도록 함
            sorted_task = sorted(task_count.items(), key=lambda x: x[1])
            # task_count가 빌 때까지 매 cycle을 순회
            for i in range(n + 1):
                # 현재 cycle에서 가능한 모든 task를 돌았으면 나머지는 idle이므로 for문 탈출
                if not sorted_task:
                    break
                # 현재 가장 많이 남은 task를 뽑아서 count를 빼줌
                task, _ = sorted_task.pop()
                task_count[task] -= 1
                # 모든 count를 다 쓴 task(완전히 수행한 task)는 제거해줌
                if task_count[task] == 0:
                    del task_count[task]
                cycle += 1
            
            # 마지막 task를 수행할 경우(cycle)를 제외하고 answer에는 항상 idle만큼 채워서 쿨다운 + 1만큼의 시간을 소요함
            answer += (n + 1) if task_count else cycle

        return answer
