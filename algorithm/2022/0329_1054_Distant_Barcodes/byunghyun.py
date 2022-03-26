class Solution:
    # barcode 리스트를 포함된 요소와 그 요소의 개수로 바꾸어서 반환하는 함수
    # time Limit Exceed 문제를 피하기 위해 여기에서 미리 개수를 기준으로 오름차순으로 정렬하여 반환한다
    # 요소 리스트와 요소의 개수 리스트를 순서에 맞추어서 정렬해야 하기 때문에
    # 넘파이의 argsort를 이용하여 index_list를 얻고 이 index_list를 이용하여 요소 리스트를 재정렬해주었다.
    def make_pair(self, target_list):
        import numpy as np
        keys = set(target_list)
        keys = list(keys)
        keys_count = []
        for key in keys:
            keys_count.append(target_list.count(key))
        sorted_keys_count = np.sort(keys_count)
        sort_index = np.argsort(keys_count)
        sorted_keys = []
        for i in sort_index:
            sorted_keys.append(keys[i])
        return list(sorted_keys), list(sorted_keys_count)
    
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        len_barcodes = len(barcodes)
        # result를 0으로 초기화한다.
        self.result = []
        for _ in range(len_barcodes):
            self.result.append(0)
        # make_pair 함수를 이용하여 정렬된 요소 리스트를 얻어낸다.
        # 요소의 리스트를 keys라 하고, 요소의 개수 리스트를 values라 하였다.
        keys, values = self.make_pair(barcodes)
        index = 0
         
        for _ in range(len(keys)):  
            # 개수가 많은 것부터 차례로 꺼낸다.
            target_value = values.pop()
            target_key = keys.pop()
            
            #개수만큼 해당 요소를 채워넣는다.
            for _ in range(target_value):
                self.result[index] = target_key
                # 하나씩 건너뛰며 요소를 넣어간다.
                index += 2
                # result의 홀수 번째 공간을 다 채웠다면, result의 짝수 번째 공간을 채워나간다.
                if index >= len_barcodes:
                    index = 1
        return self.result
