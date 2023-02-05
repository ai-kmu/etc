import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        # 빌딩마다 point들을 시작점과 끝점 같이 저장
        for b in buildings:
            points.append([b[0], b[2], 's'])
            points.append([b[1], -b[2], 'e'])

        # points 정렬을 x값은 작은 것부터, 높이 값은 큰 것부터 정렬
        points.sort(key=lambda x: (x[0], -x[1]))

        max_h = [0]
        ans = []

        # heapq는 최소값이 root에 
        for p in points:
            if p[2] == 's':
                if p[1] > -max_h[0]: # 시작점인 경우 max_h에 있는 '-최소값'보다 크면 
                    ans.append([p[0], p[1]]) # 현재 포인트의 x값과 높이값을 정답 리스트에 저장
                heapq.heappush(max_h, -p[1]) # 높이의 음수값을 heap_h에 저장. 음수를 붙이는 이유는 heap의 root가 최소값이므로
            elif p[2] == 'e': # 끝점인 경우 
                max_h.remove(p[1]) # max_h에서 현재 포인트의 '-높이'를 제거
                heapq.heapify(max_h) # heapify해서 가장 작은 값을 root로(인덱스 0번째로) 설정
                if -p[1] > -max_h[0]: # 현재 포인트의 높이와 max_h의 최소값이 둘 다 음수이므로 -붙여서 비교
                    # 현재 포인트의 높이가 max_h에 있는 높이보다 크면 현재 포인트의 x값과 max_h의 최소값의 음수값을 높이로 저장
                    ans.append([p[0], -max_h[0]]) 
        return ans
