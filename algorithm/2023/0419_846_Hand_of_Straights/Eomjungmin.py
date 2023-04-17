class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # hand 크기가 groupSize를 나눌 때 나누어 떨어지지 않은 경우 바로 false return
        if len(hand) % groupSize != 0:
            return False

        # 카드 숫자별 갯수를 dict 형태로 생성
        nums_dict = {}
        for n in hand:
            try:
                nums_dict[n] += 1
            except:
                nums_dict[n] = 0
                nums_dict[n] += 1
        
        # dict 생성 후 key 오름차순대로 정렬
        nums_dict = dict(sorted(nums_dict.items()))

        # dict의 key들을 리스트 형태로 변형 후 리스트 힙 형태로 변경
        nums_keys = list(nums_dict.keys())
        heapq.heapify(nums_keys)

        # nums_key에 원소가 있으면 맨 앞의 dict key값(for문에서 i값)부터 꺼내어
        # 이 dict key값 이후로 groupSize만큼 연속된 수들이 다 dict의 키값으로 있어야 함
        # 만약 하나라도 dict의 키에서 없는 경우 false return
        # 또한 키로 있더라도 이미 카드가 다 소진된 상태이면 역시 false return
        # 이 두 외의 경우에는 해당 키의 개수값에서 -1씩 차감하고
        # 차감한 이후 만약 현재 보고있는 i 키의 카드 갯수가 0인 경우 nums_key에서 pop시킴
        while nums_keys:
            key = nums_keys[0]
            for i in range(key, key+groupSize):
                if i not in nums_keys:
                    return False
                if nums_dict[i] == 0:
                    return False
                else:
                    nums_dict[i] -= 1
                if nums_dict[i] == 0:
                    heapq.heappop(nums_keys)
        return True
