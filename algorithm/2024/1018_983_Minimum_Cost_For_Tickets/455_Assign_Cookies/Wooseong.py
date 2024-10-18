class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 크기순으로 정렬
        s.sort()
        g.sort()

        answer = 0
        # 쿠키를 다 쓰거나 모든 애들한테 나눠줄 때까지
        while s and g:
            # 제일 욕심많은 애 (g[-1])한테 제일 비싼 쿠키 (s[-1]) 주기
            # 줄 수 있다면 애랑 쿠키 pop하고 answer += 1
            if g[-1] <= s[-1]:
                g.pop()
                s.pop()
                answer += 1
            # 줄 수 없다면 애만 버리기
            else:
                g.pop()
        
        return answer
