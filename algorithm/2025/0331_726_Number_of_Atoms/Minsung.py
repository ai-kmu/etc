from collections import defaultdict

def is_digit(a):
    return True if ord(a)>=ord('0') and ord(a)<=ord('9') else False

def is_lower(a):
    return True if ord(a)>=ord('a') and ord(a)<=ord('z') else False

def is_upper(a):
    return True if ord(a)>=ord('A') and ord(a)<=ord('Z') else False

def is_parentheses(a):
    return True if ord(a)==ord('(') or ord(a)==ord(')') else False

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        st = list()  # for stack
        # formula += '1'
        formula_index = 0
        cur_atom = ''
        counter = dict()  # 특정 atom이 몇 번 등장하였는지 저장
        atom_counter = defaultdict(int)  # 중복된 atom을 특정하기 위함
        while formula_index < len(formula):
            cur_c = formula[formula_index]  # 현재 character
            
            if is_lower(cur_c):
                cur_atom += cur_c
            
            else:
                if cur_atom != '':  # 저장된 atom 저장, counting
                    counter[f'{cur_atom}_{atom_counter[cur_atom]}'] = 1
                    st.append(f'{cur_atom}_{atom_counter[cur_atom]}')
                    atom_counter[cur_atom] += 1
                if is_upper(cur_c):
                    cur_atom = cur_c
                if formula_index == len(formula)-1:  # formula의 마지막이 alphabet이거나 괄호일 경우, 예외처리
                    if is_parentheses(cur_c):
                        break
                    if not is_digit(cur_c):
                        counter[f'{cur_atom}_{atom_counter[cur_atom]}'] = 1
                        break
                if not is_upper(cur_c):  # 대문자도 소문자도 아니라면  ->  숫자나, 괄호라면
                    st.append(cur_c)
                    cur_atom = ''
                    if is_digit(cur_c):
                        cur_digit = ''  # 두자리수까지 감안하여, 현재 digit 계산
                        while formula_index < len(formula) and is_digit(formula[formula_index]):
                            cur_digit += formula[formula_index]
                            formula_index += 1
                        formula_index -= 1
                        st.pop()
                        cur_digit = int(cur_digit)
                        if st[-1] == ')':  # digit 이전이 괄호라면
                            st_index = -2  # index of stack
                            parentheses_cnt = 1
                            while parentheses_cnt != 0:  # digit 이전의 괄호와 쌍의 괄호를 만난다면 break
                                if st[st_index]==')':
                                    parentheses_cnt += 1
                                elif st[st_index]=='(':
                                    parentheses_cnt -= 1
                                else:  # 괄호가 아닌 atom이라면
                                    counter[st[st_index]] *= cur_digit
                                st_index -= 1
                                
                                
                        else:  # digit 이전이 atom이라면
                            counter[st[-1]] *= cur_digit
                            
            formula_index += 1

        ans_counter = defaultdict(int)  # atom의 중복성을 제거하여 계산
        for key, value in counter.items():
            ans_counter[key.split('_')[0]] += value
        key_list = sorted(list(ans_counter.keys()))
        ans = ''
        for key in key_list:
            if ans_counter[key] != 1:
                ans += f'{key}{ans_counter[key]}'
            else:
                ans += key
        return ans
