#시간초과 코드
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        elements = [] #순열을 만들때 사용될 숫자들의 리스트
        permutation = [] #순열을 담을 리스트
        seq = '' #조합될 배열
        
        #순열을 만들때 사용될 숫자들을 elements 리스트에 다 넣는다
        for i in range(1, n+1):
            i = str(i)
            elements.append(i)
        
        #회귀와 for문을 사용해서 순열 배열을 생성
        def recursion(seq, arr, length):
            if length == 0:
                permutation.append(seq)
                return 
                
            for i in range(length):
                recursion(seq + arr[i], arr[:i] + arr[i+1:], length-1)
        
        #처음 회귀함수를 사용하기 위한 for문 실행
        for i in range(n):
            recursion(seq + elements[i],elements[:i] + elements[i+1:], n-1)

        
        return permutation[k-1]
    
'''우선 for문을 이용해서 elements에서 하나의 숫자를 가져와서 seq에 더하고
가져온 숫자를 제외한 나머지 숫자들의 elements들을 다시 함수에 넣어줌
이렇게 하면 elements = ['1','2','3']이라고 할때
seq = '1' elements = ['2','3']이 만들어지고 다시 회귀 함수를 통하여
seq = '12' elements = ['3'] , seq = '13' elements = ['2']의 과정을 거침
마지막으로 length가 0일때 즉 elements들을 다 사용했을 때
seq = '123' , seq = '132'  permutation에 저장
이런식으로 2와 3을 시작으로 하는 회귀함수도 통과하게 되면
['123','132','213','231','312','321']이 생성된다.'''
