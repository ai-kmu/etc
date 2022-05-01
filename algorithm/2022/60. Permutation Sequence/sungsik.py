class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return "1"
        
        # 1! 부터 (n-1)!을 담는 배열 생성
        # 사용하지 않는 0번째도 있는 이유는 단순히 index를 맞쳐주기 위함
        facts = [1] * n
        facts[1] = 1
        for i in range(2, n):
            facts[i] = facts[i-1] * i
        
        answer = ""
        # 사용가능한 숫자는 1부터 n까지
        candidates = list(range(1, n+1))
        # 현재 위치를 저장하는 pos는 n - 1 부터 시작
        for pos in range(n-1, 0, -1):
            # 현재 위치에서 아직까지 사용하지 않은 숫자가 (pos)!만큼 등장하며
            # 따라서 k를 facst[pos]로 나눈 몫이 k번째의 숫자가 되며
            tmp = (k - 1) // facts[pos] + 1
            answer += str(candidates[tmp-1])
            # 이를 candidates에서 제거한다.
            candidates.pop(tmp-1)
            # 다만 반복이 진행됨에 따라 k를 facts[pos]로 나눈 나머지로 다시 설정한다.
            k %= facts[pos]
            # pos를 1씩 감소시킨다.
            pos -= 1
        answer += str(candidates[0])
        return answer
        
