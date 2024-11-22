'''
[1,4], 2
-> 1:
    -1 < 1 => [1, 3], 2
-> 4:
    3 < 4 => [4, 6], 4
return 4

[1,2], 2
-> 1:
    [1, 3], 2
-> 2:
    3 > 2 => [1, 4], 3
return 3
'''

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        answer = 0
        before_s = -1  # 이전 공격 시점
        before_e = -1  # 이전 공격으로 인해 중독이 풀리는 시점
        before_p = 0   # 중첩을 포함해 이전 공격으로 인한 중독 시간
        for attack in timeSeries:
            # 중독이 풀린 상태면
            if attack > before_e:
                answer += duration   # 그냥 duration 더하고
                before_s = attack    # before_s 업데이트하고
                before_p = duration  # before_p는 그냥 duration이 됨
            # 중독이 안 풀렸으면
            else:
                # 이번 공격으로 인해 중독이 풀리는 시점 구해서
                after_e = attack + duration
                # 이전 공격으로 인한 중독 시간 빼고
                answer -= before_p
                # 중독시간은 (이전 공격 시점 ~ 이번 공격으로 인해 중독이 풀리는 시점)이니까
                before_p = (after_e - before_s)
                # 그거 더해줌
                answer += (after_e - before_s)
            # before_e 업데이트는 동일
            before_e = attack + duration
        
        return answer
                
