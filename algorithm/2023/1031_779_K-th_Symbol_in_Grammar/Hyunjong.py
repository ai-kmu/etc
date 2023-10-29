class Solution:
    def kthGrammar(self, n, k):
        # n행에 있는 개수를 계산
        num_ele = 2**(n - 1)

        # 플래그 초기화
        is_same = True

        # 반복
        for _ in range(1, n):
            num_ele //= 2

            # 다음 조건일 때 k를 조정하고 플래그 변경
            if k > num_ele:
                k -= num_ele
                is_same = not is_same

        return 0 if is_same else 1
