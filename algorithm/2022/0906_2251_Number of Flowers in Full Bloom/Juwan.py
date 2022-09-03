from bisect import bisect_left, bisect_right

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        
        table = {} # 중복되는 사람은 해시 테이블을 이용해서 바로 구할 것.
            
        start, end = zip(*flowers) # 시작과 끝을 각각 start, end 리스트에 나눠서 저장
        
        start = sorted(list(start)) # 시작 시기를 정렬
        end = sorted(list(end)) # 끝 시기를 정렬
        answer = []
        
        for i in persons: # 사람마다 검사하는데
            
            if i in table:
                
                answer.append(table[i]) # 이미 동일한 결과는 바로 answer에 저장해줌
                
            else:
                s = bisect_right(start, i) # i라는 숫자가 시작 지점들에서 순서상 어느 곳에 위치해야할 지 찾음.
                                           # 이때, 들어가야할 위치를 오른쪽에 들어간다는 가정
                e = bisect_left(end, i) # i라는 숫자가 시작 지점들에서 순서상 어느 곳에 위치해야할 지 찾음
                                        # 이때, 들어가야할 위치를 왼쪽에 들어간다는 가정
                table[i] = s - e # 이 사람이 방문했을 때 꽃이 피어있는 개수를 s - e를 통해 구할 수 있음
                answer.append(s - e)
        
        return answer
    
    # 로직이 복잡하니 궁금하시면 물어봐주세요.
