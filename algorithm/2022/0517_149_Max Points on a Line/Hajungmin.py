class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        # 길이가 1,2 일 경우 점의 개수도 1,2이기 때문에 바로 반환
        if length < 3: 
            return length
        
        answer = 0
        
        for i in range(length):
            # 기울기가 무한대인 경우를 딕셔너리에 추가
            dic = {'inf':0}
            same = 1
            for j in range(i, length):
                if i == j:
                    continue
                # x가 같고 y값이 다를 경우 -> 기울기가 무한대일 경우
                if points[i][0] == points[j][0] and points[i][1] != points[j][1]:
                    dic['inf'] += 1
                    
                # x값이 다를 경우
                elif points[i][0] != points[j][0]:
                    grad = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    if grad not in dic:
                        dic[grad] = 1
                    else:
                        dic[grad] += 1
                # 위의 두 경우를 제외하면 같은 점이기 때문에 same에 1을 더해줌
                else:
                    same += 1
            # 현재 답과 비교하며 갱신
            answer = max(answer, max(dic.values()) + same)
        return answer
