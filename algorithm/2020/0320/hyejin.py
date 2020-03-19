# 시간복잡도 너무 느림. 더 좋은 방법 없나.
from collections import deque


def solution(priorities, location):
    answer = 0
    queue = deque()
    # 대기 순서대로 index를 queue에 넣음.
    for i in range(len(priorities)):
        queue.append(i)

    while queue:
        # 현재 idx를 queue에서 뺐는지 안뺐는지 check
        subtract = True
        # 맨앞 index
        idx = queue.popleft()
        idx_priority = priorities[idx]

        # 중요도가 더 높은 문서가 있는지 search를 해야하는데, priorities list는 크기가 너무 큼.
        # search 시간을 조금 줄이기 위해서 set을 사용. (priority 1~9) 최대 9개만 검사
        # => 만약 priority의 개수가 element보다 크다면 쓰면 안됌.
        set_priorities = set(priorities)

        for compare_prior in set_priorities:
            # 중요한 문서가 있다면 뒤로 보냄. subtract 실패
            if idx_priority < compare_prior:
                queue.append(idx)
                subtract = False
                break
        if subtract:
            priorities[idx] = -1
            answer += 1
            if location == idx:
                break

    return answer
