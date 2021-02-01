class Solution:
    def minFlips(self, target: str) -> int:
        count = 0 # 카운트 세는 변수 선언
        if target[0] == "1":
            count+=1 # target이 처음부터 1이면 하나 카운트

        else: pass

        for i,j in zip(target, target[1:]):
            if i != j:
                count+=1 # target의 한 요소와 그 다음 요소가 서로 다를 때 카운트한다.
                # 이웃한 요소가 다르면 숫자를 바꿔야하는 것이기 때문이다.

        print(count)
