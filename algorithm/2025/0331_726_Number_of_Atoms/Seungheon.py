# failcode
# failcode


from collections import defaultdict
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """

        # 사이에 1 추가
            # 대문자 대문자
            # 대문자 (
            # 대문자 )

            # 소문자 대문자
            # 소문자 (
            # 소문자 )

            # ) 대문자


        # 마지막에 1 추가
            # )
            # 대문자
            # 소문자


        big_alphabat_set = set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        small_alphabat_set = set(list("abcdefghijklmnopqrstuvwxyz"))
        nums_set = set(list("0123456789"))

        # 1 넣기
        new_formula = ""
        for i, formula_char in enumerate(formula[:-1]):
            new_formula += formula_char 
            # 대문자
            if formula_char in big_alphabat_set:
                # 대문자
                if formula[i+1] in big_alphabat_set:
                    new_formula += '1'
                # 소문자
                if formula[i+1] == "(":
                    new_formula += '1'
                if formula[i+1] == ")":
                    new_formula += '1'
            # 소문자
            elif formula_char in small_alphabat_set:
                # 대문자
                if formula[i+1] in big_alphabat_set:
                    new_formula += '1'
                # 소문자
                if formula[i+1] == "(":
                    new_formula += '1'
                if formula[i+1] == ")":
                    new_formula += '1'
            
            elif formula_char == ")" :
                if formula[i+1] == ")": # ) )
                    new_formula += '1'
                if formula[i+1] in big_alphabat_set: # ) 대문자 
                    new_formula += '1'

        new_formula += formula[-1]
        if formula[-1] in big_alphabat_set or formula[-1] in small_alphabat_set or formula[-1]==")":
            new_formula += '1'

        print(new_formula)

        # 괄호 단위로 자르기
        formula_chunk_list = []
        prv_chunk_idx = 0
        for i in  range(len(new_formula)):
            if new_formula[i] == '(' or new_formula[i] == ')' :
                formula_chunk_list.append(new_formula[prv_chunk_idx:i]) # 이전 까지
                formula_chunk_list.append(new_formula[i]) # 괄호
                prv_chunk_idx = i + 1
        
        formula_chunk_list.append(new_formula[prv_chunk_idx:])

        print(formula_chunk_list)

        formula_list = []
        chunk_idx = 0
        while chunk_idx < len(formula_chunk_list):
            if formula_chunk_list[chunk_idx] == ')':
                tmp_answer = ''

                mul_noise_list = re.findall(r'[A-Za-z]+|\d+', formula_chunk_list[chunk_idx + 1])
                mul_int = int(mul_noise_list[0])
                formula_chunk_list[chunk_idx + 1] = ''.join(mul_noise_list[1:])

                while 1:
                    poped_formula = formula_list.pop() # 변환할 수식 추출
                    if poped_formula == '(':
                        break
                    else:
                        tmp_answer += poped_formula

                splited_tmp_answer = re.findall(r'[A-Za-z]+|\d+', tmp_answer) # 숫자 영어 분리
                                
                # 숫자에 괄호 밖 숫자 곱하기
                tmp_splited_tmp_answer = ''
                for formula_tmp_idx ,formula_tmp in enumerate(splited_tmp_answer):
                    if formula_tmp_idx % 2 == 1: # 숫자면
                        tmp_splited_tmp_answer += str(int(formula_tmp) * mul_int)
                    else:
                        tmp_splited_tmp_answer += formula_tmp
                
                # list에 변환된값 추가
                formula_list.append(tmp_splited_tmp_answer)
                chunk_idx += 2
            else:
                # ')'가 아니면 list에 추가
                formula_list.append(formula_chunk_list[chunk_idx])
                chunk_idx += 1

        print(formula_list)

        answer = defaultdict(int)
        for formula_chunk in formula_list:
            formula_chunk_splited = re.findall(r'[A-Za-z]+|\d+', formula_chunk)
            for idx in range(len(formula_chunk_splited)//2):
                answer[formula_chunk_splited[idx*2]] += int(formula_chunk_splited[idx*2+1])

        answer_text = ''    
        for key in sorted(answer.keys()):
            answer_text += key
            if answer[key] != 1:
                answer_text += str(answer[key])


        return answer_text
        # dictionary와 text 결합하여 dictionary 만들기
