from bisect import bisect_left


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        answer = []
        n = len(potions)
        # 이분 탐색을 위한 정렬
        potions.sort()

        # spells를 순회
        for spell in spells:
            # success를 넘는 최소 인덱스를 찾음
            now_success = success / spell
            # bisect_left : 이분탐색 시 만족하는 인덱스의 왼쪽 인덱스를 반환
            idx = bisect_left(potions, now_success)
            # 성공하는 경우를 구해야 하므로 potion의 길이에서 뺀 값을 answer에 추가
            answer.append(n - idx)

        return answer
