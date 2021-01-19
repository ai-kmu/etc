class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0 # 받아들이는 리스트 길이가 3 미만이면 0출력
        
        bigger = [0] * n # 큰 수 count
        smaller = [0] * n # 작은 수 count
        result = 0 # 결과 저장
        
    
        for i in range(n - 1):
            for j in range(i + 1, n):
                if rating[j] > rating[i]: 
                    bigger[i] += 1 # 인덱스 j의 값이 인덱스 i의 값보다 크면 bigger값을 +1씩 증가시킴
                else:
                    smaller[i] += 1 # 인덱스 j의 값이 인덱스 i의 값보다 작으면 smaller값을 +1씩 증가시킴
        

        for i in range(n - 2):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    result += bigger[j] # 점점 커지는 경우 저장(rating[i]<rating[j]<rating[k])
                else:
                    result += smaller[j] # 점점 작아지는 경우 저장(rating[i]>rating[j]>rating[k])
        
        return result
