class Solution:
    def maxJump(self, stones: List[int]) -> int:
    # test case는 통과이나 submit 이후 막힘
        if len(stones) == 3:
            return stones[2]
        ans = stones[1]

        for i in range(2,len(stones),2):
            if ans < stones[i] - stones[i-2]:
                ans = stones[i] - stones[i-2]

        if len(stones) % 2 !=0:
            for j in range(len(stones)-1,0,-2):
                if j == 1:
                    break

                if ans < abs(stones[j-2] - stones[j]):
                    ans = abs(stones[j-2] - stones[j])
                    print(ans)
        else:
            for j in range(len(stones)-2,0,-2):
                if j == 1:
                    break

                if ans < abs(stones[j-2] - stones[j]):
                    ans = abs(stones[j-2] - stones[j])
                    print(ans)

        return ans
