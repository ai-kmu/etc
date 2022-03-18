class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        #양쪽 괄호는 항상 왼쪽은 여는 괄호, 오른쪽은 닫는 괄호니까
        #num_of_case = 나올수 있는 경우의 수
        num_of_case = 2*n-2
        for i in range(2**num_of_case):
            #경우의 수를 편하게 만들기 위해 이진수 변환을 활용한다.
            test_target = bin(i)[2:].zfill(num_of_case)
            if test_target.count('0') == test_target.count('1'):
                tmp_tester = 0
                test_pass = True
                #순환하면서 닫는 괄호가 여는 괄호보다 많은 순간이 있는지 검사
                for tmp in test_target:
                    if tmp == "0":
                        tmp_tester+=1
                    else:
                        tmp_tester-=1
                    if tmp_tester < -1:
                        test_pass = False
                # 유효하다면
                if test_pass == True:
                    test_target = '0'+test_target+'1'
                    test_target = test_target.replace("0", "(")
                    test_target = test_target.replace("1", ")")
                    self.result.append(test_target)
                    
        if num_of_case == 0:
            self.result.append("()")
        
        return self.result
