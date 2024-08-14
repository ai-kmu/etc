# Solution 참조
# https://www.youtube.com/watch?v=4WQouWU9XXE
class Solution(object):
    
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr_sort = sorted(arr)
        arr_list = []
        arr_len = len(arr)

        # 만약 이미 sorting되어 있는것으면 pass
        if arr == arr_sort :
            pass
        # 아닐경우 10 * arr.lenght만큼 돌아도 상관없기 때문에 제일 큰수를 뒤로 보내는 것을 하는 전략
        # 먼저 전체에서 제일 큰 것을 앞으로 가져오고, 다시 뒤집어서 제일 큰 것을 뒤로 보냄
        # 초기 arr에서 제일 큰 것을 기준으로 indexing을 하나씩 줄이면서 list를 정렬
        else:
            for i in range(arr_len):
                max_ = max(arr[:arr_len - i])
                max_index = arr.index(max_) + 1
                arr[:max_index] = reversed(arr[:max_index])
                arr_list.append(max_index)
                arr[:arr_len - i] = reversed(arr[:arr_len - i])
                arr_list.append(arr_len - i)

        return arr_list