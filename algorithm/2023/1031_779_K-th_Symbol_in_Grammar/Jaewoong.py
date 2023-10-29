# 정답보고 공부했습니다.
class Solution:
    def kthGrammar(self, n, k):
        # k값과 첫 element가 동일한지 확인하는 플래그 초기화
        are_values_same = True

        # n번째에서 전체 element의 개수는 2^(n-1)
        n = 2**(n - 1)

        # 첫 row 도착까지 반복
        while n != 1:
            # 절반 줄임
            n //= 2

            # k가 절반 이후에 있으면 k값 줄이고 플래그를 false로 조정
            if k > n:
                k -= n
                are_values_same = not are_values_same

        # 값이 똑같으면 0, 아니면 1
        return 0 if are_values_same else 1
