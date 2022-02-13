class Solution:
    
    ## 원리: left를 기준으로 수집할 수 있는 fruit의 최대 범위를 구함(sliding window)
    
    ### (1) 과일 종류가 2개 이상이 되기전까지 r을 증가: 수집할 수 있는 최대 과일 수
    ### (2) 과일 종류가 2개 이상이 될 경우 left 기준을 오른쪽으로 이동시킴
    ### 예: 3,3,1,2,2,2  -> 3,3,1까지는 right만 증가 이후 2가 들어오면서 fruit type을 줄이기위해서 2개의 3을 제거 이후 다시 right 증가 

    from collections import defaultdict
    def totalFruit(self, tree): 
        answer = 0                            # the number of fruit   
        count = defaultdict(int)              # dicionary(Hash Table) 생성: int(default: 0)

        left = 0                                 # 기준 index
        for right, fruit in enumerate(tree):
            count[fruit] += 1                    # fruit tree에 있는 fruit의 개수 저장
            
            ## 과일 종류가 2개 이상이 될경우, 기준 index를 오른쪽으로 옮겨가며 과일 종류를 2개로 맞춰줌
            while len(count) > 2:               # basket에 서로 다른 fruit type이 두개 이상 들어간 경우
                count[tree[left]] -= 1          # 가장 이전의 들어왔던 fruit의 1개를 제거 

                if count[tree[left]] == 0:      # 가장 이전의 들어왔던 fruit의 1개를 제거 
                    del count[tree[left]]       # dictionary에서 해당 fruit type을 제거(key)
                left += 1                       # 기준 index를 오른쪽으로 옮김(+1)

            answer = max(answer, right - left + 1)  

        return answer
