class Solution(object):
    def candy(self, ratings):
        N = len(ratings)
        canndy = [] ## 이웃하는 값에 대한 상대적인 사탕개수이므로 앞 뒤 2방향을 고려하기 위해 사탕개수를 따로 따로 관리해야 한다.
        for i in range(N): ## 최소 1개의 사탕
            canndy.append(1)

        for i in range(1 , N): ## ratings 앞 방향으로 사탕 개수 고려
            if ratings[i] > ratings[i-1]: ## 앞에 아이보다 뒤의 아이가 랭크가 더 높은 경우
                if canndy[i-1] +1 > canndy[i]: ## 뒤에 아이가 앞의 아이보다 사탕이 적으면
                    canndy[i] = canndy[i-1] + 1 ## 앞의 아이 사탕 개수 +1를 뒤의 아이에게 주면 된다.
        
        for i in range(N-2 , -1, -1): ## ratings 뒤 방향으로 사탕 개수 고려
            if ratings[i] > ratings[i+1]: ## 뒤의 아이보다 앞의 아이가 랭크가 더 높은 경우
                if canndy[i+1] +1 > canndy[i]: ## 앞의 아이가 뒤의 아이보다 사탕이 적으면
                    canndy[i] = canndy[i+1] + 1 ## 뒤의 아이 사탕개수 +1를 앞의 아이에게 주면 된다.
        
        max_ = sum(canndy)               
        return max_
