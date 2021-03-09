# def is_available(candidate, current_col):
#     current_row =  len(candidate)
#     for queen_row in range(current_row):
#         if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
#             return False
#     return True
#
# def DFS(N, current_row, current_candidate, final_result):
#     if current_row == N:
#         final_result.append(current_candidate[:])
#         return
#
#     for candidate_col in range(N):
#         if is_available(current_candidate, candidate_col):
#             current_candidate.append(candidate_col)
#             DFS(N, current_row+1, current_candidate, final_result)
#             current_candidate.pop()
#
# def solve_n_queens(N):
#     final_result = []
#     DFS(N, 0, [], final_result)
#     return final_result
import sys

sys.setrecursionlimit(1000)

def isAvailable(currentCandidate, currentCol):
    currentTotalRow = len(currentCandidate)

    for currentRow in range(currentTotalRow):
        if currentCandidate[currentRow] == currentCol or abs(currentCandidate[currentRow] - currentCol) == currentTotalRow - currentRow:
            return False
    return True


def dfs(N, currentRow, currentCandidate, finalResult):
    if currentRow == N:
        finalResult.append(currentCandidate[:])
        return

    for currentCol in range(N):
        if isAvailable(currentCandidate, currentCol):
            currentCandidate.append(currentCol)
            dfs(N, currentRow + 1, currentCandidate, finalResult)
            currentCandidate.pop()


def solveNQueens(N):
    finalResult = []
    dfs(N, 0, [], finalResult)
    return finalResult


print(solveNQueens(10))