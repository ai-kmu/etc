def solution(A, B):
    A = sorted(A)
    B = sorted(B)
    lst = []
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] < B[j]:
                lst.append(B[j])
                B.remove(B[j])
                break
    return len(lst)
