class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 먼저 가지수를 셀 수 있는 1차원 배열을 만든다.
        # 이 때, 마지막 인덱스에는 총 가지수를 반환할 수 있도록 한다.
        method = [0] * (amount + 1)
        methode[0] = 1

        # coin들을 돌아가며 amount를 나타낼 수 있는 가지수를 모두 센다.
        for currcoin in coins:
            # 현재의 amount를 계산하며 총 amount와 같을 경우 method[-1]에 가지수가 추가되도록 한다.
            for curramount in range(currcoin, amount + 1):
                # 현재 코인이 만약 2라면 지불 할 수 있는 금액이 2부터이므로 반복문을 돌 때, 현재 코인인덱스 부터 시작한다.
                # 현재 amount 에서 코인을 뺀 인덱스를 현재 amount 인덱스에 더하게 되는데 이건 이전까지 계산한 값을 다시 사용하려는 목적으로 memoization과 동작이 유사함
                method[curramount] += method[curramount - currcoin]
        # 최종 방법의 가지수를 반
        return method[-1]
    
