#이 코드를 해석하시는 분들께 감사의 말씀을 드립니다.
from collections import Counter 
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        if len(barcodes) == 1:
            return barcodes 
        
       
        most_value = Counter(barcodes).most_common()[0][0] #제일 많은 원소를 찾기.
        answer = [most_value] #제일 많은 원소를 answer이란 리스트의 처음에 배치한다음, 넣었으니까 barcodes에서 삭제하는 코드 
        
        for i in range(len(barcodes)): 
            if barcodes[i] == most_value: 
                barcodes.pop(i)
                break
                
        stack = []
        for i in range(0, len(barcodes)):                       
            if answer[-1] != barcodes[i] and len(stack) == 0: #stack이 비어있고 answer의 끝원소와 barcodes원소가 같으면 barcodes에 집어 넣기
                answer.append(barcodes[i])
             
              
            elif answer[-1] == barcodes[i]: #answer의 마지막원소와 barcodes[i]가 같으면 stack에 넣어두기 
                stack.append(barcodes[i])
                
                
            elif answer[-1] != barcodes[i] : 
                answer.append(barcodes[i])
                answer.append(stack.pop())
        
        #코드는 복잡하지만 원리는 간단하다. 제일 많은 원소를 맨 앞에 배치한다음, answer의 마지막 원소와 bacodes[i]가 다르면 answer에 붙이고 
        #겹치면 stack에다가 보관하는 형식으로 하였다. 
        #신기한 점은 answer의 마지막원소와 bacodes[i]가 다른 경우 
        #stack의 마지막원소를 barcodes[i]와 answer[-1]을 둘 다 비교한다음 stack에서 꺼내서 집어넣어야 하는데,
        #무지성으로 붙였는데도 잘 돌아갔다. (속도도 빠르다.)
       
        
    
        #가끔 stack에 남아있는 원소가 있어서 정렬한 길이와 원래 barcodes의 길이가 같지 않을 수 있다.
        #이럴 때는 하나씩 stack에서 꺼내서 정렬 된 answer의 원소중 같지 않은 원소들 사이에 강제로 집어넣었다. 
        
        if len(answer) == len(barcodes) + 1:
            return answer
                
        else:      
            for stack_value in stack:   
                for i in range(1, len(answer)-1): 
                    if answer[i-1] != stack_value and answer[i] != stack_value:
                        answer.insert(i, stack_value)
                        break
        return answer
        
