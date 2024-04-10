from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        # 각 nums의 숫자와 등장횟수를 구함
        # num1, num2, num3까지 만들 수 있는 숫자와 숫자를 만들 수 있는 경우의 수를 구함 => counter2
        # num4와 연산하여 0을 만들 수 있는 개수를 answer 에 더함

        answer = 0

        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        counter3 = Counter(nums3)
        counter4 = Counter(nums4)

        new_counter1 = defaultdict(int)
        new_counter2 = defaultdict(int)

        for c1 in counter1.keys():
            for c2 in counter2.keys():
                new_counter1[c1+c2] += counter1[c1] * counter2[c2]
        
        for nc1 in new_counter1.keys():
            for c3 in counter3.keys():
                new_counter2[nc1+c3] += new_counter1[nc1] * counter3[c3]

        for nc2 in new_counter2.keys():
            if -nc2 in counter4:
                answer += new_counter2[nc2] * counter4[-nc2]

        return answer
