# greedy 알고리즘으로 품

# 색칠 문제와 비슷
# 이웃한 칸은 같은 값이면 안된다.
# 단 채울 수 있는 value의 수는 정해져 있다.
# 그러면 우선 가장 많은 수의 value들을 먼저 할당하면 된다.

from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes):
        # 가장 빈도수가 높은 순으로 정렬한 dictionary를 만듦, 이 때 key값은 숫자값(barcodes[idx])이고 value는 value의 빈도수
        data = {}
        keys = []
        for k,v in Counter(barcodes).most_common():
            data[k] = v
            keys.append(k)
        
        ans = [0] * len(barcodes)
        flag = -2 # 21번째 줄에서 첫번째 값 역시 general하게 설정시켜주기 위해 -2로 할당
        for i in range(len(barcodes)):
            if len(keys) > flag+1 and data[keys[flag + 1]] >= data[keys[0]]:
                flag+=1
            else:
                new_flag = 0
                while(data[keys[new_flag]] == 0 or new_flag == flag):
                    new_flag+=1
                flag = new_flag


            ans[i] = keys[flag]
            data[keys[flag]]-=1
            
        
        return ans
