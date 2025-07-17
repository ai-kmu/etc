class Solution:
    def backtrack(self, target_value, count, start, combination, results):
        if target_value < 0 or count < 0:
            return

        if target_value == 0 and count == 0:
            results.append(list(combination))
            return

        for i in range(start, 10):
            if i > target_value:
                break
            
            combination.append(i)
            self.backtrack(target_value - i, count - 1, i + 1, combination, results)
            combination.pop()

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        combination = []

        self.backtrack(n, k, 1, combination, results)

        return results
