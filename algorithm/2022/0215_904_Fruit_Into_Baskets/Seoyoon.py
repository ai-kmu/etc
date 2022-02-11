class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        ## Sliding Window 풀이
        
        # 빈 딕셔너리 생성
        cnt = {}
        # 반복할 i, 결과 저장할 res를 초기값 0으로 지정
        i = res = 0 
        
        # j를 이용해 오른쪽 끝까지 이동(전체 탐색)
        for j,v in enumerate(tree):
            cnt[v] = cnt.get(v,0)+1 #cnt.get(v,0): 딕셔너리에서 v찾고 없으면 0
            
            # 길이가 2보다 초과되면 오른쪽 끝점에서 -1처리
            while len(cnt)>2:
                cnt[tree[i]] -=1
                if cnt[tree[i]] == 0:
                    del cnt[tree[i]]
                i+=1
                
            # 간격의 길이가 가장 긴 것 return
            res = max(res, j-i+1) 
        return res
