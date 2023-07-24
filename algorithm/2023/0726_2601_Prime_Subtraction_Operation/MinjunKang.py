# 솔루션

def isPrime(x: int) -> bool:
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x %i == 0:
            return False
    return True

def primeSubOperation(nums: List[int]) -> bool:
    p = 0
    for x in nums:
        if x <= p:
            return False
        prime = x - p - 1
        while prime > 0 and not isPrime(prime):
            prime -= 1
        if prime == 0:
            p = x
        else:
            p = x - prime
    return True
