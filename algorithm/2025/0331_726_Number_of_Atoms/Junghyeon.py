# 안에서부터 다 벗기고 -> 딕셔너리로 개수 세고 -> 합치기

# K4(ON(SO3)2)2 -> K4(ONSO3SO3)2 -> K4ONSO3SO3ONSO3SO3

# K4 O N S O3 S O3 O N S O3 S O3

from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        dictionary = defaultdict(int)

        # 괄호 있는 동안 다 벗겨야함
        while "(" in formula and ")" in formula:
            for i in range(len(formula)):
                if formula[i] == "(":
                    idx1 = i
                # 처음 만나는 ")"가 제일 안에 있는 괄호
                if formula[i] == ")":
                    idx2 = i
                    j = idx2 + 1
                    mm = ""
                    while j < len(formula) and formula[j].isdigit():
                        mm += formula[j]
                        j += 1
                    
                    if mm:
                        mult = int(mm)
                    else:
                        mult = 1

                    # "ABC" * 3 = "ABCABCABC"임을 이용
                    a = formula[idx1+1:idx2] * mult
                    
                    formula = formula[:idx1] + a + formula[j:]
                    break
                    
        i = 0

        # 다 벗긴 atom에서 하나씩 숫자 세기
        while i < len(formula):
            if formula[i].isupper():
                atom = formula[i]
                i += 1
                while i < len(formula) and formula[i].islower():
                    atom += formula[i]
                    i += 1
                
                cnt_str = ""
                while i < len(formula) and formula[i].isdigit():
                    cnt_str += formula[i]
                    i += 1

                if cnt_str:
                    cnt = int(cnt_str) 
                else:
                    cnt = 1
                dictionary[atom] += cnt
            else:
                i += 1

        # 딕셔너리에서 값 꺼내서 최종 결과 만들기
        result = ""
        for atom in sorted(dictionary.keys()):
            result += atom + (str(dictionary[atom]) if dictionary[atom] > 1 else "")

        return result
