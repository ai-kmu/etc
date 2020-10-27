'''
#Magical String
S= "1221121221221121122……"

#Magical String을 연속되는 1과 2로 각각 그룹 지음
1 22 11 2 1 22 1 22 11 2 11 22 ......

#각 그룹의 개수를 계산
1 2 2 1 1 2 1 2 2 1 2 2 ......

#이러한 성질을 이용해서 Magical String을 원하는 길이만큼 만들 수 있음

122로 시작해보면
1.
- 첫번째 숫자인 1은 어떤 숫자그룹이 1개로 구성됨을 의미
- 두번째 숫자인 2는 어떤 숫자그룹이 2개로 구성됨을 의미
- 세번째 숫자인 2는 어떤 숫자그룹이 2개로 구성됨을 의미

2. 첫번째 숫자와 두번째 숫자는 이미 122니까 구성된 숫자 확인
따라서 세번째 숫자부터 확읺해보면
세번째 숫자인 2는 어떤 숫자그룹이 2개로 구성됨을 의미하는데 원본 Magical String을 보면 122(11)임을 확인
규칙을 찾아보면 현재 String의 마지막 숫자와 다른 숫자(현재는 1)에 대해 현재 가리키는 숫자(현재는 2, 세번째 숫자부터 시작)만큼 생성해서 concatenate해주면 됨


'''


class Solution(object):
    def magicalString(self, n):

        S = [1,2,2]
        idx = 2

        #주어진 숫자 n만큼 만들어질 때까지 반복
        while len(S) < n:
            print(S[idx],[(3 - S[-1])])
            #Magical String S 생성
            S += S[idx] * [(3 - S[-1])]
            print(S)

            idx += 1
        #Magical String의 첫 N개 중에서 1의 개수 계산
        return S[:n].count(1)

if __name__ == '__main__':
    s=Solution()
    print(s.magicalString(7))


'''
2 [1]
[1, 2, 2, 1, 1]

1 [2]
[1, 2, 2, 1, 1, 2]

3
'''