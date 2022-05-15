# 모든 경우의 점들로 직선 만들어서 그때의 기울기를 구하자

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 1 # 모든 점은 최소 한 라인 위에 있어야 하기 때문에 최소가 1
        for i in range(len(points)-1): # 모든 점을 반복한다. (j=i+1이므로 마지막 점은 x)
            # 모든 새 점에 대한 dictionary 생성
            dic = collections.defaultdict(lambda:1) # 모든 점을 1로 초기화한다. 
            x, y = points[i][0], points[i][1] #x1, y1
            for j in range(i+1, len(points)):   # 우리는 나머지 점을 확인해야한다.
                if points[j][0] == x:   # 기울기가 무한대일 때: x=n (예외)
                    dic['inf'] += 1
                else:
                    k = (y-points[j][1])/(x-points[j][0]) # 기울기 구함((y-y1/x-x1))
                    dic[k] += 1
            ans = max(ans, max(dic.values())) # 최대의 점의 개수 구함

        return ans
