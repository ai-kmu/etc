class Solution:
    def candy(self, ratings):
        left = [1 for i in range(len(ratings))]
        right = [1 for i in range(len(ratings))]
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1
                
            if ratings[-i] < ratings[-(i+1)]:
                right[-(i+1)] = right[-i]+1
            
        return sum([max(right[i], left[i]) for i in range(len(right))])
