from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 앨리스는 카드 몇장을 갖고 있음
        # 이들을 정렬하길 원함
        # 그룹으로 정렬하는데 그룹의 크기가 있음
        # 그룹은 연속적

        cnt_nums = Counter(hand) # 각 숫자의 개수를 파악
        while cnt_nums:
            n = groupSize
            current = min(cnt_nums.keys()) # 가장 작은 수부터 시작하는데
            while n: # 그룹 사이즈만큼 loop를 돎
                if current not in cnt_nums: # 만약 불연속이 된다면
                    return False # False를 리턴
                cnt_nums[current] -= 1 # 그게 아니라면 해당 숫자를 사용했으니 감소 시킴
                if cnt_nums[current] == 0: # 만약 해당 숫자를 다 썼다면
                    del cnt_nums[current] # Counter 딕셔너리에서 삭제
                current += 1
                n -= 1

        return True
