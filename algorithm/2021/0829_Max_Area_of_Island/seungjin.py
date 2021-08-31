def max_area(grid):
    m ,n = len(grid) , len(grid[0])
    def mapping(i,j):
        global area
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        if grid[i][j] == 0:
            return 0
        grid[i][j] = 0

        return 1 + mapping(i+1 , j) + mapping(i , j+1) \
        +mapping(i-1 , j) + mapping(i , j-1)

    areas = []
    for col in range(m):
        for row in range(n):

            if grid[col][row] == 1:
                areas.append(mapping(col,row))

    print(areas)
    return max(areas)
