## pair를 만들 때 규칙 
## (1) 최초로 괄호를 넣거나 혹은 괄호 개수("("와 ")")가 같을 경우: "("를 추가
## (2) 열린괄호 "("가 입력 개수 만큼 될 경우: 닫힌 괄호(")")르 추가 / 더이상 열린 괄호가 등장하면 paranthess 생성이 어려움
## (3) 열린 괄호가 닫힌 괄호보다 많지만 아직 1번이나 2번의 경우가 아닐 경우: 닫힌 괄호를 추가 후 열린 괄호도 추가해준다.
class Solution:
    def generateParenthesis(self, num):

        result = []

        ## 재귀 함수의 파라미터 의미
        ## left: 열린 괄호, "("의 사용 개수, right : 닫힌 괄호 ")"의 사용 개수  

        def pair(result, string, num, left, right):
            print(result, string, num, left, right)
            ## 1번의 경우(최초로 괄호가 시작 or 시작 괄호 개수 == 닫힘 괄호 개수) => 열린 괄호를 추가
            if left == 0 or left == right:
                string +='('                             # 열린 괄호 추가
                pair(result, string, num, left + 1, right)  # 열린 괄호 개수 추가 

            ## 2번의 경우(재귀 함수 간의 열린 괄호가 입력 개수만큼 사용)
            elif left == num:

                remain = left - right

                ## 사용되지 않은 닫힌 괄호만큼 반복문 활용해 닫힌 괄호 만든 후 list에 추가 
                for _ in range(remain):
                    string +=')'

                # 완성된 짝을 list에 저장 
                result.append(string)

            ##  3번의 경우 열린 괄호가 닫힌 괄호보다 많을 경우
            elif left > right:
                pair(result, string +')', num, left, right + 1)
                pair(result, string +'(', num, left + 1, right)
        pair(result,'', num, 0, 0)
        return result
