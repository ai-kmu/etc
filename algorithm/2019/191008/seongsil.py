#1
def dfs(tickets, answer):
    
    if tickets == []:
        return answer
    
    left = [i for i in range(len(tickets)) if tickets[i][0] == answer[-1]]
    if not left:
        return None
    
    left.sort(key = lambda i: tickets[i][1])
    
    for i in left:
        a = dfs(tickets[:i]+tickets[i+1:], answer+[tickets[i][1]]) 
        if a is not None:
            return a        


def solution(tickets):
    start = ["ICN"]
    answer = dfs(tickets, start)
    
    return answer
    
    
    
    
