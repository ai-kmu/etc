class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        empty_cells = []
        surplus_stones = []

        for row in range(3):
            for col in range(3):
                value = grid[row][col]

                if value == 0:
                    empty_cells.append((row, col))
                    continue

                if value > 1:
                    surplus_stones.extend([(row, col)] * (value - 1))

        total_empty = len(empty_cells)
        INF = float("inf")
        dp = [INF] * (1 << total_empty)
        dp[0] = 0

        for state in range(1 << total_empty):
            filled_count = state.bit_count()

            if filled_count == total_empty:
                continue

            target_r, target_c = empty_cells[filled_count]

            for stone_idx in range(total_empty):
                if state & (1 << stone_idx):
                    continue

                stone_r, stone_c = surplus_stones[stone_idx]
                next_state = state | (1 << stone_idx)
                move_cost = abs(target_r - stone_r) + abs(target_c - stone_c)

                dp[next_state] = min(dp[next_state], dp[state] + move_cost)

        return dp[(1 << total_empty) - 1]
