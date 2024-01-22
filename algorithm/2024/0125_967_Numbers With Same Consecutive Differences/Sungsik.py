class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        answer = set([str(x) for x in range(1, 10)])
        # 1부터 9까지 추가한 후, n-1번 돌면서 k만큼 더하거나 뺌
        for _ in range(n-1):
            new_answer = set()
            for prev in list(answer):
                last = int(prev[-1])
                # k를 더한 값 추가
                if last + k < 10:
                    new_answer.add(prev + str(last + k))
                # k를 뺀 값 추가
                if last - k >= 0:
                    new_answer.add(prev + str(last - k))
            answer = new_answer
        return [int(x) for x in list(answer)]
