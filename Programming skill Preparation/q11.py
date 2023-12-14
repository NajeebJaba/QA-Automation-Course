# Question 11

#Suppose you have a grid of n x m cells, where each cell is either empty or contains a rock.
#You're given a starting position in the grid (x,y), and you want to reach a target position (tx,ty),
#but you can only move in four directions (up, down, left, right) and you can only move through empty cells.You're also given a limited number of moves k that you can make.
#Write a program to determine if it's possible to reach the target position from the starting position within k moves.


def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def reach_target_position(grid, start, target, k):
    def dfs(x, y, moves_left):
        if (x, y) == target:
            return True

        if moves_left == 0:
            return False

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, n, m) and grid[new_x][new_y] == 0:
                grid[new_x][new_y] = 1  # Mark the cell as visited
                if dfs(new_x, new_y, moves_left - 1):
                    return True
                grid[new_x][new_y] = 0  # Backtrack

        return False

    n, m = len(grid), len(grid[0])
    start_x, start_y = start
    target_x, target_y = target

    if abs(start_x - target_x) + abs(start_y - target_y) > k:
        # The Manhattan distance is greater than the available moves
        return False

    return dfs(start_x, start_y, k)

# Test the program

# #matrix 4 x 5
# grid = [
#     [0, 0, 0, 0, 0],
#     [1, 1, 0, 1, 1],
#     [0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0],
# ]
# start_position = (0, 0)
# target_position = (3, 4)
# available_moves = 5
#
# result = reach_target_position(grid, start_position, target_position, available_moves)
# print("Can reach target within available moves:", result)


