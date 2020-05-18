def solution(answers):
    people = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    results = []
    for person in people:
        results.append(sum([n == person[i%len(person)] for i, n in enumerate(answers)]))
        
    return [i + 1 for i, result in enumerate(results) if max(results) == result]
