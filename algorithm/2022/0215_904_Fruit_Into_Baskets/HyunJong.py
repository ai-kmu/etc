class Solution(object):
    def totalFruit(self, fruits):
        # fruits = [1,2,3,2,2]
        # 왼쪽부터 오른쪽으로 과일 나무가 한 줄로 늘어진 농장
        # 리스트 요소 값 : 나무 열매 종류
        # 규칙을 지키며 최대한 많은 열매를 수집하는 문제
        # 1. 2개의 바구니를 가지고 있고 각각의 바구니에는 오직 한 종류의 과일만 담을 수 있다.
        # 2. 선택한 나무에서(index) 시작하여 오른쪽으로 이동하는 동안 모든 나무의 열매를 하나씩 따야 한다. 이때 딴 열매는 바구니에 들어가야 한다
        # 3. 바구니에 들어갈 수 없는 열매가 달린 나무에 도착하면 멈춰야 한다.

        # 3종류의 과일이 담기기 전까지는 딕셔너리에 추가하면서 개수를 저장한다.
        # 3종류의 과일이 바구니에 담기는 경우 while문을 통해서 새로운 과일이 담기기 바로 이전의 연속된 같은 과일을 갖고 다시 카운팅 하도록 한다.
        # [1,2,1,1,3,3,3]일때 1,2,1,1을 보고 새로운 3이 들어오면 3 바로 앞의 1,1을 갖은 상태로 3부터 다시 카운트 하도록 한다. -> 임종수님 코드
        
        # 변수 초기화한다.
        baskets = {} # 바구니
        last_tree_idx = 0 # pointer 역할  
        answer = 0 # return 값
        count = 0 # 나무 열매 개수 저장용 변수

        for i in range(len(fruits)): # 완전 탐색
            if fruits[i] not in baskets and len(baskets) < 2: # 열매가 새로운 종류이고 바구니에 2종류 이하의 열매가 있을 때 
                baskets[fruits[i]] = 1 # 바구니에 열매를 넣는다.
            elif fruits[i] in baskets: # 바구니에 있는 열매 종류일 때 
                baskets[fruits[i]] += 1 # 바구니에 열매를 넣는다.
            
            while(fruits[i] not in baskets and len(baskets) ==2): # 열매가 새로운 종류이고 바구니에 2종류의 열매가 있는 동안
                if(baskets[fruits[last_tree_idx]] == 1): # 지난 나무 열매 종류가 1개가 있을 때
                    baskets.pop(fruits[last_tree_idx]) # 지난 나무 열매를 바구니에서 제거하고
                    baskets[fruits[i]] = 1 # 새로운 종류의 나무 열매를 바구니에 넣는다
                else: # 지난 나무 열매 종류가 2개 이상이면
                    baskets[fruits[last_tree_idx]] -= 1 # 열매 개수를 한개 줄이고
                count -= 1 # 전체 열매 개수를 줄인다.
                last_tree_idx += 1

            count +=1 # 전체 열매 개수를 늘린다.
            answer = max(answer,count)

        return answer
