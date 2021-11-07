class Solution:
    def candy(self, ratings: List[int]) -> int:
        # greedy algorithm
        n = len(ratings)
        # minimum candy
        candies = [1] * n
        
        # forward
        # 만약 앞의 이웃보다 rating이 높을 경우
        # 이전 이웃보다 사탕을 하나 추가한다.
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        # backward
        # 만약 뒤의 이웃보다 rating이 높을 경우
        # 뒤의 이웃보다 사탕을 하나 추가한다.
        # 다만, 뒤의 이웃보다 사탕을 하나 추가한 수가
        # forward 때에 구한 사탕의 수보다 적을 경우 변경하지 않는다.
        for i in reversed(range(n-1)):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
        
        return sum(candies)
