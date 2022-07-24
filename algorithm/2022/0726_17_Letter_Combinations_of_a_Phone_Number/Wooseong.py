class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''숫자에 대응하는 str list 설정'''
        num_to_list = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        '''하드 코딩'''
        d = len(digits)
        if not d:
            return []
        elif d == 1:
            A = num_to_list[digits[0]]
            return [A[i] for i in range(len(A))]
        elif d == 2:
            A = num_to_list[digits[0]]
            B = num_to_list[digits[1]]
            return [A[i] + B[j] for i in range(len(A)) for j in range(len(B))]
        elif d == 3:
            A = num_to_list[digits[0]]
            B = num_to_list[digits[1]]
            C = num_to_list[digits[2]]
            return [A[i] + B[j] + C[k] for i in range(len(A)) for j in range(len(B)) for k in range(len(C))]
        elif d == 4:
            A = num_to_list[digits[0]]
            B = num_to_list[digits[1]]
            C = num_to_list[digits[2]]
            D = num_to_list[digits[3]]
            return [A[i] + B[j] + C[k] + D[l] for i in range(len(A)) for j in range(len(B)) for k in range(len(C)) for l in range(len(D))]
        
        '''while로 푸는 방법도 있는데 얘는 너무 느려서 오히려 안 좋음'''
#         if not d:
#             return []
#         else:
#             i = 0
#             temp = ['']
#             '''한 글자 씩 이어 붙이는 방법'''
#             while i < d:
#                 A = temp
#                 B = num_to_list(digits[i])
#                 temp = [A[i] + B[j] for i in range(len(A)) for j in range(len(B))]
#                 i += 1
                
#             return temp
            
