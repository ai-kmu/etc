#Greedy를 활용하여 인덱스를 기반으로 제일 작은 값을 고르게 하였다.
#오답

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        answer = triangle[0][0]
        if len(triangle) == 1:
            return min(triangle[0])
        
        answer += min(triangle[1])
        summed_index = triangle[1].index(min(triangle[1]))
        if len(triangle) == 2:
            return answer
        for i in range(2, len(triangle)):
            if summed_index == len(triangle) - 1:
                answer += min(triangle[i][summed_index], triangle[i][summed_index - 1])
                summed_index = triangle[i].index(min(triangle[i][summed_index], triangle[i][summed_index - 1]))
            else:
                answer += min(triangle[i][summed_index], triangle[i][summed_index + 1])
                summed_index = triangle[i].index(min(triangle[i][summed_index], triangle[i][summed_index+1]))
        return answer
