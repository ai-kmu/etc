from collections import defaultdict

class Solution:
    def mulAtoms(self, formula: str, idx: int):
        """
        괄호로 묶인 Atoms 처리 (재귀)
        
        Input
            formula: representing a chemical formula, str
            idx: 현재의 위치 인덱스, int
        Return
            atom_dict: 괄호 처리된 누적 Atom Dict, dict
            idx: 현재의 위치 인덱스, int
        """
        atom_dict = defaultdict(int)
        tmp = ""

        while idx < len(formula):
            f = formula[idx]

            if f == "(":  # 괄호 만나면 재귀적으로 처리
                sub_dict, newIdx = self.mulAtoms(formula, idx + 1)
                idx = newIdx  # 괄호 끝나고는 그 다음 인덱스로 이동

                # 괄호로 묶인 원자 개수 처리 (multiply)
                num = ""
                while idx < len(formula) and formula[idx].isdigit():
                    num += formula[idx]
                    idx += 1
                num = int(num) if num else 1

                for k, v in sub_dict.items():
                    atom_dict[k] += v * num

            elif f == ")":
                idx += 1
                break

            # 원자 시작
            elif f.isupper():
                # 만약 이전에 저장한 원자가 있다면 먼저 dict에 저장해줌
                if tmp:
                    atom_dict[tmp] += 1
                tmp = f
                idx += 1

            elif f.islower():
                tmp += f
                idx += 1

            elif f.isdigit():
                num = f
                idx += 1
                while idx < len(formula) and formula[idx].isdigit():
                    num += formula[idx]
                    idx += 1
                atom_dict[tmp] += int(num)
                tmp = ""

        # 마지막에 남은 원자 처리
        if tmp:
            atom_dict[tmp] += 1
            
        return atom_dict, idx


    def countOfAtoms(self, formula: str) -> str:
        """
        Input
            formula: representing a chemical formula, str
        Return
            ans: the count of each atom(in sorted order), str
        """
        atom_dict, _ = self.mulAtoms(formula, 0)
                
        atom_dict = sorted(atom_dict.items())
        ans = ""
        for k, v in atom_dict:
            ans += k
            if v != 1:
                ans += str(v)
    
        return ans
