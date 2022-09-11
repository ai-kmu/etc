class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
    '''
    모든 sub-sequence의 합을 구한다 -> dp
    if 최대 값  > (10^9+7) / k     ->   return 10^9 + 7
    elif 최대값 < 0    ->  return 0
    else return 최대 값 * k
    '''
    dp = []
    
