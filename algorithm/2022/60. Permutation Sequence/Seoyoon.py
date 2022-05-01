# (지양) 가장 먼저 접근한 방식은 모든 조합을 다 구한뒤 k번째 순열을 return 하기 (근데 시간초과 안뜸(?))
from itertools import permutations
class Solution:
    def getPermutation(self, n,k):
        comb_list = []
        for i in range(n):
            comb_list.append(str(i+1)) # 모든 원소 넣고

        result = []
        for i in permutations(comb_list, n):
            result.append(i) # 모든 조합 구해서

        return ''.join(result[k-1]) # k번째 조합 return

# 다른 방법: 먼저 맨 앞글자를 찾고 그다음 수를 찾자. 찾을때 몫과 나머지를 이용해보자
# 예를 들어 n=4 k=9의 경우 맨 앞자리가 1,2,3,4 총 4개가 올 수 있고 
# 맨앞자리 고르고 나면 그 뒤에는 무조건 3!번씩 온다. 즉, (n-1)!번씩 온다. 
# 이걸 이용하면 n=4 일때 k=9번째 순열을 찾고프면 앞자리가 2일때 있을 것. (앞에 6개(3!)는 앞자리가 1이니까)
# 이 때의 2는 9를 3!으로 나눈 몫인 1에다가 1을 더한 값임. 
# 9를 3!으로 나눈 나머지는 3이 되고 이 3을 다시 k로 써서 이하 자리들을 구해나가면 된다.  

class Solution(object):
    def getPermutation(self, n, k):
        answer = ''
        fact = [1] * n # 가능한 조합 수(팩토리얼) 저장할 리스트 생성
        num = [] # 1~n까지 원소를 저장할 리스트 생성
        
        # num 리스트에 일단 모든 원소를 다 넣어둔다.
        for i in range(n):
            num.append(str(i+1)) # str씌워야 원하는 형태로 출력 가능
            
        # fact 배열에는 n!을 구해서 넣음 ex) n=4일때 1,1,2,6
        for i in range(1, n):
            fact[i] = fact[i - 1] * i
        k -= 1
        
        #이제부터 각 자리에 해당하는 값을 반복문으로 구할것
        #뒤에서부터 돌면서 (4,3,2,1) 이순서로 넣어야 첫자리부터 구할수있음
        for i in range(n, 0, -1):
            # 첫번째 자리는 (n-1)!으로 나눈 몫을 인덱스로 해서 그때의 원소로 정함
            first = k // fact[i - 1] # 몫
            # 나머지 결과를 다시 k에 할당하여 k를 갱신해서 다시 이하 자리 구함
            k %= fact[i - 1]
            # 해당인덱스(first)의 원소(num[first])를 하나의 자리로 정했고, answer에 넣는다.
            # (원래 몫이 1이면 그다음 숫자 2로 해야하는데 리스트 index 특성(0부터) 때문에 1 안더하는게 맞음. 그래서 그냥 num[first])
            answer += num[first] 
            # 하나 정했으니까 pop 하고 다른자리 구하러 다시 for문으로 들어감
            num.pop(first) 
        return answer
