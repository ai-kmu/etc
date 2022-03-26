from collections import Counter 
import heapq

class Solution:
    #주어진 barcodes 배열에서 각 숫자별 빈도수를 세어서 가장 높은 빈도수를 갖는 두개의 숫자를 불러와서 나열하면 양 옆에 숫자가 겹쳐지지 않고 잘 나열된다.
    #이때 숫자의 빈도수를 카운트 하기 위해서 카운터를 사용했고 가장 높은 빈도수를 갖는 숫자를 찾기 위해서 최대힙을 사용했다.
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        answer = []
        hq = []
        
        #바코드 배열에 있는 숫자들의 빈도수를 카운트하기 위해서 카운터 사용 그 값들은 튜플의 형태로 리스트에 저장
        count_barcordes = Counter(barcodes).items()
        
        #카운트된 바코드의 튜플(숫자,빈도수)들을 힙에 넣는데 빈도수가 높은 순서대로 위에 오게 하기 위해서 최대힙을 사용하기 떄문에 빈도수에 -붙힘
        for key,value in count_barcordes:
            heapq.heappush(hq,(-value,key))
        
        #힙에서 두개의 값을 뽑아올 수 있을때까지 반복
        #빈도수가 가장 높은 두개의 숫자를 가져와서 정답 리스트에 차례대로 넣음
        #그리고 값을 뽑았기 때문에 빈도수(=value)에 +1 더함 (최대힙을 사용했기 때문에 value가 음수로 되어있음)
        while len(hq) > 1:
            first_value, first_key = heapq.heappop(hq)
            second_value, second_key = heapq.heappop(hq)
            
            
            answer.append(first_key)
            answer.append(second_key)
            
            first_value += 1
            second_value += 1
            
            #만약 뽑아온 숫자의 빈도수가 0보다 클 경우 다시 힙에 넣어서 진행하고 만약 빈도수가 0인 경우에는 다시 힙에 넣지 않음
            if first_value < 0 :
                heapq.heappush(hq, (first_value,first_key))
            if second_value < 0 :
                heapq.heappush(hq, (second_value,second_key))
        
        #만약 숫자가 다 나가고 1개만 남은 경우 혹은 처음부터 숫자가 1개가 들어온 경우를 처리하기 위한 if문
        if len(hq) == 1:
            value, key = heapq.heappop(hq)
            answer.append(key)
            
            
        return answer
                
