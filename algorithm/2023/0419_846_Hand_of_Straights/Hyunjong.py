class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """

        # 각 요소 값이 몇개인지 조사
        num_count = {}
        for taget in hand:
            keys = num_count.keys()
            if taget in keys:
                num_count[taget] = num_count[taget] + 1
            else:
                num_count[taget] = 1

        # 정렬된 상태에서 하나씩 조사
        for num in sorted(hand):
            if num_count[num] > 0:
                for i in range(groupSize-1, -1, -1):
                    # 앞의 수보다 뒤의 수가 무조건 크거나 같아야 한다.
                    if num + i not in num_count or num_count[num + i] < num_count[num]:
                        return False
                    # 뒤의 수는 앞의 수만큼 사용된다.
                    num_count[num + i] = num_count[num + i] - num_count[num]
        return True
