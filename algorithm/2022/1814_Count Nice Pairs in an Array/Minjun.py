from collections import Counter

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # 시간을 효율적으로 하기위해서
        # i + rev(j) = j + rev(i) 을 찾는 것을
        # i - rev(i) = j - rev(j) 로 관점을 바꿔서 접근한다.
        # -> 요소 자신과 reverse한 값의 차가 같은 요소들을 찾으면 된다.
        
        # nums를 i - rev(i) 로 계산한다.

        diff = [] # i - rev(i) 저장할 리스트 생성
        for num in nums:
            diff.append(num - int(str(num)[::-1]))
        
        counter = Counter(diff)    
        
        answer = 0
        
        for i in counter.values():
            
            if i > 1: # 차가 같은 요소가 존재하는 경우에만 계산
                answer += i * (i - 1) // 2 # 조합공식으로 푼다
        
        return answer % (10**9+7) 
