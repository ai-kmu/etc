class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev_steps_list = [1, 2]
        for i in range(3, n + 1):
            current_steps = prev_steps_list[0] + prev_steps_list[1]
            prev_steps_list[0] = prev_steps_list[1]
            prev_steps_list[1] = current_steps

        return prev_steps_list[1]
