num = int(input())

matrix = [[int(10000001) for i in range(num)] for j in range(num - 1)]


R, G, B = map(int, input().split())
First_house = [R,G,B]    
  


for i in range(1, num):
  R, G, B = map(int, input().split())
  matrix[i-1][0] = R
  matrix[i-1][1] = G
  matrix[i-1][2] = B


#print(matrix)

mins = 10000001

for k in range(3):
    stick = [First_house[k], First_house[k], First_house[k]]
    #print(stick)
    T = matrix[0][k]
    matrix[0][k] = 1000001
    for i in range(num - 1):
  #      print("\t", stick)
        new_stick = [0,0, 0]
        for j in range(3):
            if(j == 0):
                min = stick[1]
                if min > stick[2]:
                    min = stick[2]
                new_stick[j] = min + matrix[i][j]
            elif(j == 1):
                min = stick[0]
                if min > stick[2]:
                    min = stick[2]
                new_stick[j] = min + matrix[i][j]
            else:
                min = stick[0]
                if min > stick[1]:
                    min = stick[1]
                new_stick[j] = min + matrix[i][j]
        stick = new_stick
     #   print("\t", stick)
    matrix[0][k] = T

    #print("min : ", mins)
    for i in range(3):
        if i!= k:
            if mins > stick[i]:
                mins = stick[i]

print(mins)
    
