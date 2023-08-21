class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        word_list = ['a', 'b', 'c']
        
        # 예외 먼저 처리
        if k > 3 * 2 ** (n - 1):
            return ""
        
        result = []
        
        def backtrack(current):
            # 현재 문자열이 길이 n과 같으면, 리스트에 추가하고 리턴
            if len(current) == n:
                result.append(current)  
                return
            
            for char in word_list:
                # 새로운 문자 char 를 current에 추가할 수 있는지 확인후 재귀적으로 탐색
                if len(current) == 0 or char != current[-1]:
                    backtrack(current + char)  
        
        # word_list의 각 문자로 시작하여 문자열을 생성
        for char in word_list:
            backtrack(char)
        print(result)
        # 문자열을 반환
        return result[k-1]
