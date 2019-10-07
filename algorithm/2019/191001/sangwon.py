def solution(operations):
    answer = []
    op1=[]
    op2=[]
    answers=[]
    
    for i in range(len(operations)):
        sp=operations[i].split()
        op1.append(sp[0])
        op2.append(sp[1])
    op2=list(map(int,op2))
    for i in range(len(op1)):
        if op1[i]=="I":
            answers.append(op2[i])
        if op1[i]=="D" and len(answers)!=0:
            if op2[i]==1:
                answers.remove(max(answers))
            elif op2[i]==-1:
                answers.remove(min(answers))
                
    if not answers:
        answer=[0,0]
    else:
        answer=[max(answers),min(answers)]
    return answer
