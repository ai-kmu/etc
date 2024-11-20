# 홀수 => 끝
# 짝수 => 엘리스 -> 홀수 => 밥 -> 모음이 아닌 게 하나라도 있어야 지움 => 엘리스 다 지움
#                         -> 모음이 아닌가 하나도 없으면 못지움

def count_vowels(s):
    count = 0
    index = 0
    dic = {}
    for i in s:
        if i in ['a', 'e', 'i', 'o', 'u']:
            count += 1
            dic[count] = index
        index += 1
    return dic

class Solution(object):
    def doesAliceWin(self, s):
        dic = count_vowels(s)
        dic_keys = list(dic.keys())
        if dic_keys == []:
            return False
        if dic_keys[-1] % 2 != 0:
            return True
        else:
            if dic[dic_keys[-1]] + 1 == len(s):
                True
            else:
                False
        return True
