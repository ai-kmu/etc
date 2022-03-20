class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        aws_list = []
        
        
# n 을 왼쪽 오른쪽 쌓을 수 있는 개수로 취급한다. => 쌓으면 개수를 빼는 방식
# 왼쪽을 우선순위로 쌓을 수 있는 경우의 수를 탐색하는 방식 
# if left >0 다음에 if left < right를 만들어 우선 순위를 왼쪽에 주었다.
# ((())) -> (()()) -> (())() -> ()()() 순으로 탐색

        def generate(left, right, aws): 
            if left == 0 and right == 0: # 왼쪽 오른쪽 모두 다 사용한 경우
                aws_list.append(aws) # 지금 루트의 방법을 다 찾은 것이므로 append 해준다.
            if left > 0: # 왼쪽으로 쌓을 수 있는 개수가 존재할 때
                generate(left - 1, right, aws + "(") 
            if left < right: #왼쪽보다 오른쪽이 더 쌓을 개수가 많은 경우
                generate(left, right - 1, aws + ")")
        generate(n, n, "")

        return aws_list 
