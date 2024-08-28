from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        num_dict = defaultdict(int)
        result = []

        # nums의 for문을 돌려서 dictionary형태로 저장함.
        # 만약 num_dict에 해당 숫자가 있으면 value에 1을 더해줌
        # 만약 없으면 num_dict에 value를 0으로 두고 추가함
        for i in nums:
            if len(num_dict) == 0:
                num_dict[i] = 0
            else:
                if i in num_dict.keys():
                    num_dict[i] += 1
                else:
                    num_dict[i] = 0
        
        # 저장한 dict에서 value가 0인 부분만 list로 저장해서 return
        for key in num_dict.keys():
            if num_dict[key] == 0:
                result.append(key)

        return result