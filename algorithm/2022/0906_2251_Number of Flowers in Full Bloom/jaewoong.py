class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        start = []
        end = []
        # persons를 인덱스로 활용
        for x,y in flowers:
            start.append(x)
        
        for x,y in flowers:
            end.append(y)
             
        start.sort()
        end.sort()
        
        #print(start)
        #print(end)
        
        # 풀이실패....어째서 이진탐색 문제인지 감이 안잡힙니다.....
