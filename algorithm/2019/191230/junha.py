d,k=map(int,input().split())
D_num=[1,1]         #피보나치 들어갈 리스트

while True:
  if len(D_num)==d-1:
    break
  D_num.append(D_num[-1]+D_num[-2])   #동적계획법으로 체우기

a_CO=D_num[-2]  #a의 계수 coefficient
d_CO=D_num[-1]  #b의 계수 coefficient


# a와 b가 모두 1보다 큰 정수라는 것을 이용한다.
# a가 b보다 작으므로, a를 1부터 모든 양의 정수를 넣어본다. 
i=1
while True:
  diff=(k-a_CO*i)
  if diff%d_CO==0:
    a=i
    b=diff//d_CO
    break
  i+=1
  
print(a)
print(b)
