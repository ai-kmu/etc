from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 예외 처리: (example 2)
        if n == 0:
            return len(tasks)

        # Counter는 dictionary 형태로 요소들의 개수를 세 줌.
        nums = list(Counter(tasks).values())
        max_num = max(nums)  # 가장 많은 수의 task는 몇 개? (네 개)
        all_maxes = nums.count(max_num)  # max_num 만큼의 tasks가 몇 개? (A, B 두 개)
        
        # 1. (A, B, idle, ...) * (4 - 1) + (A, B)
        #    idle은 마지막에 올 필요 없으니까 (max_num - 1) 만큼만 idle 포함해서 반복하고
        #    idle 빼고 all_maxes를 반복
        #    이때 max_num보다 적은 나머지 task는 idle 자리에 대충 넣으면 알아서 처리됨.
        # 2. all_maxes가 짱 많아서 idle 없이 채울 수 있을 때
        #    ex) n = 3인데 A, B, C, D가 전부 네 개 씩 있으면
        #        A B C D A B C D A B C D A B C D 해서 끝낼 수 있음 == len
        #    p.s. example 2랑은 다른 상황임
        # 둘 중에 더 큰 걸 택해야 함 - 2가 무조건 작거나 같기 때문.
        return max((n + 1) * (max_num - 1) + all_maxes, len(tasks))
