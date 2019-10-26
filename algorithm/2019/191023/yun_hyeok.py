def solution(triangle):
    MAX_DEPTH = len(triangle)
    cache = [[None for j in range(i + 1)] for i in range(MAX_DEPTH)]
    
    def search(idx, depth):
        if idx < 0 or idx >= len(triangle):
            return 0
        if depth == MAX_DEPTH:
            return 0
        
        if cache[depth][idx] == None:
        	cache[depth][idx] = max(search(idx, depth + 1), search(idx + 1, depth + 1)) + triangle[depth][idx]
        return cache[depth][idx]

    answer = search(0, 0)
    return answer
