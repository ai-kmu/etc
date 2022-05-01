# 원래 의도 

'''
숫자에서 가장 맨뒤에있는 숫자를 기준으로 이전에 있는것드로가 하나씩 변경하면서 값과 해당 위치(개수)를 저장 후 결과를 반환하고자 함

예(최초):
123  => 132 => 231 ...

시간이 없어서 더 수정하면 될것같은데 이렇게 제출합니다. (거의 제대로 못푼것같아서 벌금 내야할것같습니다.)

'''

class Solution:
    
    # 각 위치 마다 바꿔주는 함수
    def change(self, num, i, j):
        tem = str(num[i])
        num[i] = str(num[j])
        num[j] = tem
        return num

    def getPermutation(self, n: int, k):
        
        # 먼저 가장 base 가되는 첫번째 값=> 1,2,3 => 123을 반환해주는 LOGIC
        position, n = 0, 3
        value = ''
        for i in range(1, n+1):
            value = value + str(i)
        cnt = 0
        
        # 다른 코드 참고해서 진행
        def permutations(self, num, k, point=0):
            # 종료 조건을 위해서 앞서 불러왔던 cnt 불러와서 개수 만큼 반복해서  
            if point == len(num) - 1:
                cnt +=1
                if cnt == k:
                    return  print(''.join(num))
            
            # 가장 먼저 나와있는 숫자 이후에 뒤로 있는 숫자들과 바꿔서 결과값을 비교 
            for i in range(point, len(num)):
                print(point, num, i)
                self.change(num, poin, i)
                permutations(num, poin + 1)
                self.change(num, poin, i)
        
        # 최초의 base값을 입력       
        s = value
        return permutations(self, num = list(s), k=k)
