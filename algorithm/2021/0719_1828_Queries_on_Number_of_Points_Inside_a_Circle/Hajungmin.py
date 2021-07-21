class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        
        #쿼리의 x, y, r값을 루프를 통해 받아온다.
        for x, y, r in queries:

            #answer배열에 원 안의 점의 개수를 세기위해 0을 append시켜준다.
            answer.append(0)

            #point x와 point y를 루프를 통해 받아온다.
            for px, py in points:

                #유클리드 거리를 계산하여 원의 반지름보다 같거나 작으면 answer에 1을 추가한다.
                if math.sqrt(math.pow((x-px),2) + math.pow((y-py),2)) <= r:
                    answer[-1] += 1
                    
        return answer
