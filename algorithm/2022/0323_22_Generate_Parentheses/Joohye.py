# 괄호 한쌍을 1 이라고 가정,
# ex) n=4 일때 나올 수 있는 경우의 수 ; 4 + 0,3 + 1,2 + 2,1 + 3,0 + 4 
# 3: ()()(), ((())), (()()), (())(), ()(())
# 1: ()
# 3 + 1 의 조합 : ()()()(), ((()))(), (()())(), (())()(), ()(())()

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n == 1:  # n = 1 일때 결과는 하나이므로
            return ["()"] 
        else:
            lst = self.generateParenthesis(n-1)
            answer = []
            
            for i in range(len(lst)):
                answer.append("(" + lst[i] + ")")  # (((( )))), ((( ))) 이런 경우
            
            for k in range(1, int(n/2) + 1):  # n개를 k개와 n-k개로 나누어 두 리스트를 만든다.
                k_list = self.generateParenthesis(k)
                n_k_list = self.generateParenthesis(n-k)
                
                for f in range(len(k_list)):  # 바로위 두 list 에 들어있는 값들로 조합을 만들어 푼다.
                    k_par = k_list[f]
                    for s in range(len(n_k_list)):
                        n_k_par = n_k_list[s]
                        
                        answer.append(k_par + n_k_par)  # 1 + 3 일 경우
                        answer.append(n_k_par + k_par)  # 3 + 1 일 경우 
            return list(set(answer))  # 마지막에 set, 중복값 삭제
                    
