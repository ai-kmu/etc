import heapq

class Solution(object):
    def getSkyline(self, buildings):
# 못풀어서 해답 참고했습니다

        # 정렬(처음위치와 높이 기준)
        buildings.sort(key=lambda x:[x[0],-x[2]])    
        new_b=[]
        # 가장 오른쪽의 x
        max_r=-float('inf')
        # 가장 왼쪽의 x
        min_l=float('inf')
        # buildings의 위치 변경(haep 사용을 위함)
        for i in buildings:
            new_b.append([-i[2],i[0],i[1]])    
            max_r=max(max_r,i[1])
            min_l=min(min_l,i[0])
        

        # h, x_1,x_2
        # 높이 0 , 가장 왼쪽x, 가장 오른쪽x를 가지는 bulding 생성
        ans=[[0,0,max_r+1]]              
        f_ans=[]
        
        # h에 대한 max heap
        heapq.heapify(ans)
        # 가장왼쪽x가 가장 오른쪽x보다 커질때까지
        while min_l<=max_r:

            # heapq 만들기
            # 빌딩이 남아있고, 새로운 빌딩의 x가 min_l보다 작으면 
            while new_b and new_b[0][1] <= min_l:
                # 새로운 빌딩을 pop하고 heapq에추가
                temp=new_b.pop(0)
                heapq.heappush(ans,temp)

            # answer이 있고 answer의x_2가 min_l보다 작으면 
            while ans and ans[0][2]<=min_l:
                # 빌딩을 pop
                heapq.heappop(ans)

            # f_ans가 비었거나 f_ans에 마지막 으로 추가된 값의 h와 새로 추가되는값의 h 가 같지않다면
            if not f_ans or f_ans[-1][1]!=(-ans[0][0]):
                # 가장 왼쪽값, 새로 추가되는값의 h을 정답에 추가
                f_ans.append([min_l,-ans[0][0]])

            # 빌딩이 남아있다면
            if new_b:
                # 가장 왼쪽값을 새로 추가된 값의 가장 오른쪽값과 남아있는값의 가장 왼쪽 값중 더 왼쪽의 있는값으로 사용 
                min_l=min(ans[0][2],new_b[0][1]) 
            # 빌딩이 남아있지 않다면 가장 왼쪽값은 마지막으로 추가한값의 가장 오른쪽값으로 설정
            else:
                min_l=ans[0][2]

        return f_ans
