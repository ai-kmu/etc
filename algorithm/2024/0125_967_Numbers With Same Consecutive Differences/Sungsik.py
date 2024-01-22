class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        answer = set(range(1, 10))
        # 1부터 9까지 추가한 후, n-1번 돌면서 k만큼 더하거나 뺌
        for _ in range(n-1):
            new_answer = set()
            for prev in list(answer):
                last = prev % 10
                # k를 더한 값 추가
                if last + k < 10:
                    new_answer.add(10 * prev + last + k)
                # k를 뺀 값 추가
                if last - k >= 0:
                    new_answer.add(10 * prev + last - k)
            answer = new_answer
        return list(answer)
