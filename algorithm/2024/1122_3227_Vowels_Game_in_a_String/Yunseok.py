###### 다시 생각 해봄 ######
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        next_str = s
        vowels_idx_list = []
        for idx, elem in enumerate(next_str):
            if elem in ['a', 'e', 'i', 'o', 'u']:
                vowels_idx_list.append(idx)

        # 어차피 앨리스가 시작
        # 모음이 홀수 개일 때, 한 번에 어차피 모두 가져갈 수 있음
        # 짝수이면 앨리스 차례에서 홀수 개가 되어버림
        if len(vowels_idx_list) == 0:
            return False
        else:
            return True

######################### 이전 문제 풀이 #########################
# 문제 풀이 실패
# 문제를 잘못 이해하였음
class Solution:

    def reindex_vowels_list(self, vowels_list, target_idx):
        if target_idx == -1:
            for idx in range(len(vowels_list)):
                vowels_list[idx] -= 1
            return vowels_list

        reoffset_value = vowels_list[target_idx] + 1
        for idx in range(len(vowels_list)):
            vowels_list[idx] -= reoffset_value
    
        return vowels_list


    def doesAliceWin(self, s: str) -> bool:
        # 초기화
        is_alices_turn = True
        next_str = s
        vowels_idx_list = []
        for idx, elem in enumerate(next_str):
            if elem in ['a', 'e', 'i', 'o', 'u']:
                vowels_idx_list.append(idx)

        while True:
            vowels_left_cnt = len(vowels_idx_list)
            if vowels_left_cnt == 0:
                return False
            elif vowels_left_cnt == 1 and vowels_idx_list[0] == 0:
                return True

            is_even = True if vowels_left_cnt % 2 == 0 else False
            if is_alices_turn: # 앨리스 턴은 홀수일 경우 카운트
                target_idx = vowels_left_cnt if is_even is not True else vowels_left_cnt - 1
                is_alices_turn = False
            else:
                target_idx = vowels_left_cnt if is_even is True else vowels_left_cnt - 1
                is_alices_turn = True
                if target_idx == 0:
                    vowels_idx_list = self.reindex_vowels_list(vowels_idx_list, -1)
                    next_str = next_str[1:]
                    continue

            target_idx_value = vowels_idx_list[target_idx]
            vowels_idx_list = self.reindex_vowels_list(vowels_idx_list, target_idx - 1)[target_idx:]
            next_str = next_str[target_idx_value - 1:]
