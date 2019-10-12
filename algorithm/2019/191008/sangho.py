def solution_1(tick):
    answer = []
    start = []
    t_start = []
    max_step = 0
    # start
    for i in range(len(tick)): 
        if tick[i][0] == "ICN":
            for k in range(len(tick)):
                if i !=k and tick[i][1] == tick[k][0] :
                    t_start.append(i)
                    start.append(tick[i][1])

    for z in range(len(start)):def solution_1(tick):
    answer = []
    start = []
    t_start = []
    max_step = 0
    # start
    for i in range(len(tick)): 
        if tick[i][0] == "ICN":
            for k in range(len(tick)):
                if i !=k and tick[i][1] == tick[k][0] :
                    t_start.append(i)
                    start.append(tick[i][1])

    for z in range(len(start)):
        t = []
        step = 0
        an = ["ICN"]
        an.append(start[z])
        t.append(t_start[z])
        for w in range(len(tick)):                
            for p in range(len(tick)):
                if p not in t and  an[-1] == tick[p][0] :
                    an.append(tick[p][1])
                    t.append(p)
                    step += 1 
        answer.append(an)
        if step > max_step :
            max_step = step
    print(max_step)
    if len(answer) == 1:
        return answer[0]
    else :
        dap = []
        for x in range(len(answer)):
            if len(answer[x]) == max_step:
                dap.append(answer[x])
            else : 
                return answer[0]
        if len(dap) == 1:
            return dap[0]
        else :
            re = dap[0]
            for n in range(len(dap)-1):
                if dap[n+1] < re:
                    re = dap[n+1]
    return re

# --------------------------------------------

######
# dfs #
#####

def dfs(tick,h,visit,t):    
    route = [h]
    
    if len(tick) == t:
        return (route,True)
    
    for i in range(len(tick)):
        (a,b) = tick[i]
        if (a == h) and (visit[i] == False ):
            visit[i] = True
            (p,r) = dfs(tick,b,visit,t+1)
            
            if r ==True :
                return (route + p,True)
            
            visit[i] = False
            
    return (route,False)

def solution_2(tick):
    visit = [False for o in tick]
    tick = sorted(tick)
    (answer , r) = dfs(tick,"ICN",visit,0)
    return answer 
        t = []
        step = 0
        an = ["ICN"]
        an.append(start[z])
        t.append(t_start[z])
        for w in range(len(tick)):                
            for p in range(len(tick)):
                if p not in t and  an[-1] == tick[p][0] :
                    an.append(tick[p][1])
                    t.append(p)
                    step += 1 
        answer.append(an)
        if step > max_step :
            max_step = step
    print(max_step)
    if len(answer) == 1:
        return answer[0]
    else :
        dap = []
        for x in range(len(answer)):
            if len(answer[x]) == max_step:
                dap.append(answer[x])
            else : 
                return answer[0]
        if len(dap) == 1:
            return dap[0]
        else :
            re = dap[0]
            for n in range(len(dap)-1):
                if dap[n+1] < re:
                    re = dap[n+1]
    return re

# --------------------------------------------

######
# dfs #
#####

def dfs(tick,h,visit,t):    
    route = [h]
    
    if len(tick) == t:
        return (route,True)
    
    for i in range(len(tick)):
        (a,b) = tick[i]
        if (a == h) and (visit[i] == False ):
            visit[i] = True
            (p,r) = dfs(tick,b,visit,t+1)
            
            if r ==True :
                return (route + p,True)
            
            visit[i] = False
            
    return (route,False)

def solution_2(tick):
    visit = [False for o in tick]
    tick = sorted(tick)
    (answer , r) = dfs(tick,"ICN",visit,0)
    return answer 