# 모든 순열을 구한 다음 k 번째 순열을 찾는 방식은 Time Limit Exceeded 가 발생함 (dfs 방식 사용..)
# 그래서 예를 들어, 1234 가장 앞자리가 2가 되려면 3!만큼의 순서를 지나야함
# 이렇게 팩토리얼을 이용해서 순서를 차감해가는 방식
'''
n = 6, k = 77 인 경우, permutation 배열은

 5!    4!   3!   2!   1!   0!
['1', '2', '3', '4', '5', '6'] (초기상태)
['2', '1', '3', '4', '5', '6'] 77 - 5! -> 1과 가장 가깝게 큰 2를 swap
['2', '1', '4', '3', '5', '6'] 17 - 3! -> 3과 가장 가깝게 큰 4를 swap
['2', '1', '5', '3', '4', '6'] 9 - 3! -> 4와 가장 가깝게 큰 5를 swap
...

이런 식으로 k가 1이 될 때까지 반복

'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact_idx = n
        
        # 0 ~ n 까지의 factorial를 계산한 배열 생성
        fact = [1 for i in range(n+1)]
        for i in range(2, n+1):
            fact[i] = fact[i-1] * i
        
        # 초기 순열 상태
        permutation = [str(i) for i in range(1, n+1)]
        
        # k 에서 뺄 수 있는 제일 큰 팩토리얼 값을 빼주면서 순서를 차감
        # k = 1 이 되면 loop 를 종료
        while k > 1:
            # k 보다 크지 않은 제일 큰 factorial 값 찾기
            while (fact_idx > 0) and (k - fact[fact_idx] < 1):
                fact_idx -= 1
            
            if fact_idx > 0:
                k -= fact[fact_idx]
                
                # permutation 배열의 두 수를 swap 해줌
                for j in range(n-fact_idx, n):
                    if permutation[n-fact_idx-1] < permutation[j]:
                        c = permutation[n-fact_idx-1]
                        permutation[n-fact_idx-1] = permutation[j]
                        permutation[j] = c
                        break
                              
        ans = ''.join(permutation)
        return ans
