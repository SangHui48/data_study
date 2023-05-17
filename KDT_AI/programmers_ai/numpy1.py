import numpy as np

def solution(board, bombs):
    answer = board
    x, y = board.shape
    area_1 = board[:x//2, :y//2]
    area_2 = board[:x//2, y//2:]
    area_3 = board[x//2:, :y//2]
    area_4 = board[x//2:, y//2:]
    np.where(area_1 == bombs[0], 0, area_1)
    np.where(area_2 == bombs[1], 0, area_2)
    np.where(area_3 == bombs[2], 0, area_3)
    np.where(area_4 == bombs[3], 0, area_4)
    return answer