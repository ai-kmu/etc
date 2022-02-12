class Solution:
    
    
    #3종류의 과일이 담기기 전까지는 딕셔너리에 추가하면서 개수를 저장
    #3종류의 과일이 바구니에 담기는 경우 while문을 통해서 새로운 과일이 담기기 바로 이전의 연속된 같은 과일을 갖고 다시 카운팅 하도록 함
    #[1,2,1,1,3,3,3]일때 1,2,1,1을 보고 새로운 3이 들어오면 3 바로 앞의 1,1을 갖은 상태로 3부터 다시 카운트 하도록 함
    
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        left = 0
        answer = 0
        count = 0
        
        for i in range(len(fruits)):
            while(fruits[i] not in baskets and len(baskets) ==2):
                if(baskets[fruits[left]] == 1):
                    baskets.pop(fruits[left])
                else:
                    baskets[fruits[left]] -= 1
                count -= 1
                left += 1
            
            if fruits[i] in baskets:
                baskets[fruits[i]] += 1
            else:
                baskets[fruits[i]] = 1
            
            count +=1
            answer = max(answer,count)
        
        return answer
