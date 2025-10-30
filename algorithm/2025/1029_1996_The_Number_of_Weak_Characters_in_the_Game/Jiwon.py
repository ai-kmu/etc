# 솔루션 참고

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # attack 오름차순, defense 내림차순
        properties.sort(key=lambda x: (x[0], -x[1]))
        cnt = 0
        max_defense = -1  # 임시값

        # 공격력 큰 순으로 탐색
        for a, d in reversed(properties):
            if d < max_defense:
                cnt += 1
            else:
                max_defense = d

        return cnt
