"""
This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
"""

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]


def __exists_helper__(board: list, i: int, j: int, current: str, target: str, board_visited: list):
    if i < 0 or j < 0:
        return False
    elif i >= len(board) or j >= len(board[i]):
        return False
    elif board_visited[i][j]:
        return False
    elif (len(current) + 1) > len(target):
        return False

    current += board[i][j]
    board_visited[i][j] = True
    if current == target:
        return True
    elif current[-1] != target[len(current) - 1]:
        return False

    return __exists_helper__(board, i - 1, j, current, target, board_visited) or __exists_helper__(board, i + 1, j, current, target, board_visited) or \
    __exists_helper__(board, i, j - 1, current, target, board_visited) or __exists_helper__(board, i, j + 1, current, target, board_visited)

def exists(board: list, target: str):
    result = False
    board_visited = [[False for x in range(len(board[0]))] for y in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == target[0]:
                result = result or __exists_helper__(board, i, j, "", target, board_visited)
            if result:
                return result
    return result


print(exists(board, "ABCCED"))
print(exists(board, "SEE"))
print(exists(board, "ABCB"))