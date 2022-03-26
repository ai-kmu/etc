class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        n=len(barcodes)
        ans=[0]*n
        ts=Counter(barcodes).most_common() # 가장 많은 수와 그 수의 개수를 튜플로 반환
        a=[]
        for t in ts:
            a.extend([t[0]]*t[1]) # 가장 많은 수 부터 순서대로 재배치
        
        if n%2==0: # 짝수일 때
            for i in range(n//2): # [a a b b] -> [a b a b] 이런식으로 순서를 뒤바꿔줌
                ans[2*i+1]=a[i]
                ans[2*i]=a[n//2+i]
                
        else: # 홀수일 때          
            if a[n//2]==a[n//2-1]: # [a a a b b] 인 경우 [a b a b a]로
                for i in range(n//2):
                    ans[2*i]=a[i]
                    ans[2*i+1]=a[n//2+i+1]

                ans[-1]=a[n//2]

            else:                  # [a a b b b] 인 경우 [b a b a b]로
                for i in range(n//2):
                    ans[2*i+1]=a[i]
                    ans[2*i]=a[n//2+i]

                ans[-1]=a[-1]
        
        return ans
