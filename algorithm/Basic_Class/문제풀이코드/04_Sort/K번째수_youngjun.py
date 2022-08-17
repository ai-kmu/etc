def solution(array, commands):
  # commands를 순회하면서 나온 i-1부터 j번째까지 범위의 list를 sort하고 num 번째의 수를 찾아 리스트에 담는다.
  return [sorted(array[i-1:j])[num-1] for i, j, num in commands]
