class Solution:
    def solution(self, n, k):
        # 뽑을 수 있는 카드가 하나 남아있으면 마무리 후 return
        if n == 1:
            self.result.append(self.card[0])
            return
        
        # card에서 몇 번째 index를 사용할지 결정해준다.
        # ex) n이 4일 경우 k가 6을 넘어가기 이전까지는 첫번째 카드인 1을 사용한다.
        # 이 6은 3!이고 이는 (4-1)!이다.
        index = (k-1)//self.fac_list[n-1]
        
        # 선택한 카드를 정답에 추가한 후 선택지에서 제거해준다.
        self.result.append(self.card[index])
        del self.card[index]
        
        # 새로운 k를 계산해준다.
        # ex) n이 4, k = 9일 경우
        # 위 식에 의해 index는 1이 선택되고
        # 9 - 3! * 1 = 3
        # 새로운 k로는 3이 들어가게 된다.
        new_k = self.fac_list[n-1] * index
        new_k = k - new_k
        self.solution(n-1, new_k)
        
    
    def getPermutation(self, n: int, k: int) -> str:
        # n이 1일 경우 바로 처리
        if n == 1:
            return str(1)
        
        # factorial의 중복 계산을 피하기 위해 factorial 계산 리스트를 미리 만들어두자
        self.fac_list = [1]
        for i in range(n):
            self.fac_list.append(self.fac_list[i] * (i+1))
            
        # 사용할 수 있는 숫자들을 card 리스트에 저장해두고
        # 정답을 기록할 result 리스트를 새로 만들어주었다.
        self.card = [i+1 for i in range(n)]
        self.result = []
        
        # 이제 k를 가지고 어떤 숫자를 사용해야 하는지 하나씩 탐색해나갈 것이다.
        self.solution(n, k)
        
        # 리스트 -> str 변환
        result = ''.join(str(i) for i in self.result)
        return result
