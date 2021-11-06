class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 2중 for문 시간초과
        if len(ratings) == 1:
            return 1
        
        
        num_child = len(ratings)
        candies = [1 for _ in range(num_child)]
        # 오른쪽 child만 비교하여 업데이트
        for i in range(1, num_child):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1 # 처음하는 iteration이기 때문에 무조건 그전보다 높도록
                
        # 왼쪽 child 비교하여 다시 업데이트
        for i in range(num_child-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                if candies[i] <= candies[i+1]: # i가 i+1보다 만족하면 pass지만 아니라면 업데이트
                    candies[i] = candies[i+1] + 1 # i+1보다 높도록 업데이트
        return sum(candies)
