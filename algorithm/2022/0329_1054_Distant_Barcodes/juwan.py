
from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
        most_dict = Counter(barcodes) # 빈도 수를 딕셔너리 형태로 저장
        
        keys = [key for key, value in most_dict.most_common()] # 키 값만 따로 모은 리스트
        
        ans = [0]*len(barcodes)
       
        index = 0
        
        for i in keys:
          
            count = 0
            
            while True:
                if count == most_dict[i]: # 만약 해당하는 숫자를 모두 다쓰면 그 숫자를 더 이상 쓰지 않음.
                  
                    break
                  
                ans[index], index,count = i, index+2,count+1 # ans 리스트에 1칸씩 띄어서 채워놓음
                # 예를 들어 ans = [0, 0, 0, ........, 0] 이런식이었다면
                # ans = [1, 0, 1, 0, 1, ......] 넣는 것임.
                
                if index >= len(ans): # 만약 1칸씩 띄어서 넣다 넘치면
                    index = 1 # 인덱스를 1부터 다시 시작해서, [1, 2, 1, 2, 1 ...] 이런식으로 채워 나감
        return ans
