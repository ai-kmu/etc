from collections import Counter
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        count = Counter()
        MOD = 10**9 + 7
        answer = 0
    
        for num in nums:
            # 숫자 순서를 바꾸는 코드
            num -= int(str(num)[::-1])
            # counter 클래스를 사용해서 해당 숫자가 리스트에 얼마나 있는지 찾아서 개수만큼 더해준다.
            answer += count[num]
            # count 딕셔너리에 있는 num을 1 증가시켜준다.
            count[num] += 1
            
        # return할 때는 문제에 나와있는 것처럼 숫자가 커질 것을 대비해서 mod 연산을 해준다.
        return answer % MOD
