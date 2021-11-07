# 오른쪽 사람과만 비교하면 왼쪽에서 봤을 때 문제 생긴다
# 왼쪽 사람과만 비교하면 오른쪽에서 봤을 때 문제 생긴다
# 양쪽 사람하고 동시에 비교하면 0이하의 숫자가 나올 수 밖에 없는 상황이 생긴다.
# 따라서 왼쪽 따로 오른쪽 따로 구한 다음 max값을 취하자


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
