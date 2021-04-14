from queue import PriorityQueue

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:                      # 길이가 2 미만인 경우에는 받을 곳이 안생김
            return 0
          
        que = PriorityQueue()
        for idx, el in enumerate(height):        # 우선순위 큐에 높이에 따라서 높은 것부터 나오게 -1 을 곱하여 저장
            que.put((-1*el, idx))
        
        answer = 0
        _, start = que.get()
        _, end = que.get()
        
        if end < start:                          # 처음 두 개는 미리 뽑아서 시작과 끝의 index를 저장
            temp = start
            start = end
            end = temp
        
        answer += (height[start] if height[start] < height[end] else height[end]) * (end - start - 1) # 현재까지 물이 들어갈 수 있는 크기는 (끝 index - 시작 index - 1) * (시작과 끝 중 더 낮은 높이)
        
        while not que.empty():                               # queue가 빌 때까지 반복
            _, temp = que.get()
            if temp < start:                                 # 시작보다 앞인 경우
                answer += height[temp] * (start - temp - 1)  # 높이는 더 작기 때문에 (시작 index - temp index - 1) * (temp의 높이)
                start = temp
            elif end < temp:                                 # 끝보다 뒤인 경우
                answer += height[temp] * (temp - end - 1)    # 높이는 더 작기 때문에 (temp index - 끝 index - 1) * (temp의 높이)
                end = temp
            else:                                            # 현재까지 start와 end 사이의 높이들은 물이 채워질 수 없는 곳이고 높이가 start,end 보다 낮기 때문에 
                answer -= height[temp]                       # 채워진 높이에서 temp의 높이만큼 빼기
        
        return answer
            
