# 못품

from collections import defaultdict
class Solution:
    def originalDigits(self, s: str) -> str:
        num_dict = defaultdict(int)
        num_letter_count_dict = defaultdict(list)
        number_list = ["one","two","three","four","five","six","seven","eight","nine","ten"]
        num_letter_list = ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]



        # 희소성이 높은 순으로 입력 정렬
        s = sorted(s, key = lambda x : len(str_dict[x]))

        # 각 letter의 수
        for letter in s:
            num_letter_count_dict[letter] += 1

        answer = []

        # counting
        while True:
            # 남은게 없으면 break
            if sum([n for n in str_dict.values()]) == 0:
                break

            tmp_s = sorted(list(set(str_dict)), key = lambda x : len(str_dict[x])

            # 각 letter마다 가능한 num list
            for num_str in number_list:
                for s_i in num_str:
                    if s_i in num_letter_count_dict.keys():
                        str_dict[s_i].append(num_str)

            # 가장 희소도가 높은 
            for letter in str_dict[tmp_s[0]]:
                num_letter_count_dict[letter] -= 1
                if num_letter_count_dict[letter] == 0:
                    del num_letter_count_dict[letter]


        return "?"
