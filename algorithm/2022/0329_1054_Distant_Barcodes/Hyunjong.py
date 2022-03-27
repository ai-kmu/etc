class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        # 가장 빈도가 높은 숫자 먼저 리스트에 넣는 방식
        # ex) barcodes = [1,1,1,2,2] 일 때 먼저 같은 크기의 리스트를 생성하고 [0, 0, 0, 0, 0], 가장 빈도수가 높은 1부터 배치하고 [1, 0, 1, 0, 1], 그 다음에 2를 배치하는 방식  [1, 2, 1, 2, 1]
        
        i, n = 0, len(barcodes) 
        result = [0] * n
        count_dic = dict() # 각종 변수 초기화
            
            
        for num in barcodes: # barcodes 요소 값을 key, 요소 개수를 value로 하는 dic 생성 {1: 3, 2: 2}
            if num not in count_dic.keys():
                count_dic[num] = 1
            else:
                count_dic[num] += 1        
                
        sorted_count_dic= sorted(count_dic.items(), key = lambda x: x[1], reverse=True) # 내림차순으로 정렬된 리스트 만들기 [(1, 3), (2, 2)]
        
        for k, v in sorted_count_dic: # 빈도수 높은 값부터 차례대로 리스트 생성하기
            for _ in range(v):
                result[i] = k 
                i += 2 
                if i >= n: 
                    i = 1
        # [1, 0, 0, 0, 0]
        # [1, 0, 1, 0, 0]
        # [1, 0, 1, 0, 1]
        # [1, 2, 1, 0, 1]
        # [1, 2, 1, 2, 1]
        return result
