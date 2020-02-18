subin, brother = map(int, input().split())

if subin == 0:
    answerArray = [0,1]
    subin = 1
else:
    answerArray = [subin - i for i in range(subin + 1)]

#print(answerArray)


for i in range(brother - subin + 1):
    answer = answerArray[subin+i] + 1
    if (subin + i + 1) % 2 == 0:
        answer2 = answerArray[int((subin+i+1)/2)]
        if answer2 < answer:
            answer = answer2
            T = subin + i
#             answerArray[T] = answer + 1
#            T-=1
            answerArray.append(answer)
            while(1):
                if(answerArray[T]-answerArray[T + 1]  > 1):
                    answerArray[T] = answerArray[T+1] + 1
                    T-=1
                else:
                    break
            continue
            
    answerArray.append(answer)
for i in range(subin, brother + 1):
    if(answerArray[i] - answerArray[i + 1] >1):
        answerArray
#print(answerArray)
print(answerArray[brother])
   
