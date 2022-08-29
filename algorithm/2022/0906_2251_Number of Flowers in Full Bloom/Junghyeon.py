class Solution:
    '''
    1. 꽃이 피는 시기와 지는 시기를 각각 리스트로 저장해서 정렬
    2. 이진탐색으로 각각 person이 어디에 있어야 하는지에 대한 인덱스를 리턴
    3. 인덱스 간의 차이가 정답
    person과 start, end가 같은 경우가 있어서 두개의 함수를 정의
    '''
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        # 꽃이 피는 시기에서 이진탐색을 진행하려는 함수
        def binsearch_start(x, arr):
            l = 0
            r = len(arr) - 1
            while l <= r:
                m = (l+r) // 2
                if arr[m] <= x:
                    l = m + 1
                else:
                    r = m - 1
            return l
        
        # 꽃이 지는 시기에서 이진탐색을 진행하려는 함수
        def binsearch_end(x, arr):
            l = 0
            r = len(arr) - 1
            while l <= r:
                m = (l+r) // 2
                if arr[m] < x:
                    l = m + 1
                else:
                    r = m - 1
            return l
        
        result = list()
        start_idx = list()
        end_idx = list()
        
        for i, j in flowers:
            start_idx.append(i) 
            end_idx.append(j)
            
        start_idx.sort()
        end_idx.sort()
        
        # 인덱스의 차이를 result에 저장
        for i in persons:
            result.append(binsearch_start(i, start_idx) - binsearch_end(i, end_idx))
            
        return result
