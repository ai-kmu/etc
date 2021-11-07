class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        candies = [1] * length # 학생별로 최소 1개씩은 갖아야 함
        
        for i in range(1, length): # 처음 학생부터 끝까지 순서대로 rating 대로 캔디 갯수 부여
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in range(length-2,-1,-1): # 양 이웃 rating을 고려해야하므로 역순으로 rating을 고려하여 캔디 갯수 최종적으로 부여
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1
                
        result = sum(candies)
                
        return result # 요소를 합하여 최소 필요한 캔디 갯수 구함
