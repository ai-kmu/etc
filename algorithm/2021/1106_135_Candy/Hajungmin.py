class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 사탕의 개수를 모두 1로 초기화
        candy = [1 for num in ratings]
		# 양 옆 이웃을 비교해서 사탕을 하나씩 더해준다
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candy[i]=candy[i-1]+1
        # 다시 이웃학생들을 비교해서 점수는 높지만 사탕 수가 적은 학생들에게 사탕을 더해준다
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1] and candyi]<=candy[i+1]:
                candy[i]=candy[i+1]+1

        return sum(candy)
