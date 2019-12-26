from queue import Queue

def distance(word1, word2):
    distances = 0
    for i in range(len(word1)):
        if(word1[i] != word2[i]):
            distances+=1
    return distances

def solution(begin, target, words):
    if begin not in words:
        words.append(begin)
    answer = 0
    
    wordsGraph = {}
    for w in words:
        wordsGraph[w] = []
        for w2 in words:
            if(distance(w, w2) == 1):
                wordsGraph[w].append(w2)
    print(wordsGraph)
    Q = Queue()
    Q.put(begin)
    visited = {}
    try:
        for i in words:
          visited[i] = False
        visited[begin] = True
        FIRST = wordsGraph[begin][0]

        while not Q.empty():
            answer+=1
            Qsize = Q.qsize()
            for i in range(Qsize):
                current = Q.get()
                if FIRST == current:
                    FIRST = wordsGraph[FIRST][0]
                for similar in wordsGraph[current]:
                    if similar == target:
                        return answer
                    if not visited[similar]:
                        visited[similar] = True
                        Q.put(similar)
    except:
        pass
    return 0

    
