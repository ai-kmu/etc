# 오른쪽으로 진행할때는 수의 전환, 왼쪽으로 진행할때는 수를 그대로 전달
# k가 홀수인 경우 -> 부모는 짝수이고 부모의 왼쪽 노드에 위치함
# k가 짝수인 경우 -> 부모는 홀수이고 부모의 오른쪽 노드에 위치함 (값의 변화가 일어남) 

# cnt로 값의 변화가 몇 번 일어났는지 확인하고 최종 값을 리턴

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        cnt = 0

        while n > 1:
            # k가 홀수
            if k%2 == 1:
                k = (k+1) // 2
            # k가 짝수
            else:
                k = k // 2
                cnt += 1
            n -= 1
            
        if cnt % 2 == 0:
            return 0
        else:
            return 1
