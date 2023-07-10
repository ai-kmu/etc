import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = [] # 저장할 정답 리스트
        potions.sort() # potion 정렬
        for s in spells:
            # 만약 s*potion_최대값이 success보다 작으면 0을 ans에 append하고 바로 continue
            if s * potions[-1] < success:
                ans.append(0)
                continue

            # 만약 s*potion_최소값이 success보다 크면 potion 길이크기를 ans에 append하고 바로 continue
            if s * potions[0] >= success:
                ans.append(len(potions))
                continue

            # potion에 s를 곱하는 대신에 success를 s로 나눌 때 몫을 이용하여 bisect_left 실행
            # success//s할 때 나누어 떨어지지 않는 경우 하나 더 큰 인덱스부터 count 해야하므로 bool 추가
            # 예: s=2, potions = [5,8,8], success가 16일 때 bisect_left에서 success//s하면 나누어 떨어지므로
            # bisect_left한 인덱스 결과값 2 그대로 사용
            # s = 5, potions = [1,2,3,4,5], success = 7인 경우에는 bisect_left 인덱스값이 1인데 potions[1] = 5이므로
            # success보다 작다. 따라서 bisect_left 인덱스값에 1을 더하여 2부터 사용한다.
            i = bisect.bisect_left(potions, success//s+bool(success%s))

            # ans 리스트에 유효 success 개수 저장
            ans.append(len(potions) - (i))
                
        return ans
