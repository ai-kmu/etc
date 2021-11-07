class Solution:
    def candy(self, ratings: List[int]) -> int:
        c,d=0,1 # 위치 인덱스의 개념으로 사용할 정수
        
        arr=[1]*len(ratings) # 기본 사탕 1개씩 받고 시작하니까 [1] * 인원 수로 각자 받을 사탕을 저장할 리스트를 만듦.
        
        for i in range(len(ratings)-1): # 반복문을 돌면서
            if ratings[c]<ratings[d] and arr[d]<=arr[c]: # 만약 오른쪽에 있는 아이의 rating이 더 높은데, 사탕 수가 왼쪽 아이와 같거나 적다면
                arr[d]=arr[c]+1 # 왼쪽아이보다 1개 더 추가
            c+=1 # 인덱스를 이동
            d+=1 # 인덱스를 이동
        c,d=-1,-2 # 만약 첫 번쨰 for loop를 다 돌았다면, 
        # 오른쪽 -> 왼쪽 방향으로 다시 재 탐색할 것.
        # 이 때, 리스트의 특성으로 음수의 인덱스를 활용하면 거꾸로 for loop를 돌 수 있음.
        for i in range(len(ratings)-1):                 
            if ratings[c]<ratings[d] and arr[d]<=arr[c]: # 만약 왼쪽에 있는 아이의 rating이 더 높은데, 사탕 수가 오른쪽 아이와 같거나 적다면
                arr[d]=arr[c]+1 # 오른쪽 아이보다 1개 더 추가
            c-=1 # 인덱스를 이동
            d-=1 # 인덱스를 이동
        return sum(arr) # 합계 
