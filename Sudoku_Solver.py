import numpy as np
board = [[3,0,0,8,0,1,0,0,2],
         [2,0,1,0,3,0,6,0,4],
         [0,0,0,2,0,4,0,0,0],
         [8,0,9,0,0,0,1,0,6],
         [0,6,0,0,0,0,0,5,0],
         [7,0,2,0,0,0,4,0,9],
         [0,0,0,5,0,9,0,0,0],
         [9,0,4,0,8,0,7,0,5],
         [6,0,0,1,0,7,0,0,3]]

def possible(row, column, number):
  global board
  for i in range(9):
    if board[row][i] == number:
      return False
  for i in range(9):
    if board[i][column] == number:
      return False
  block_c= (column//3)*3
  block_r=(row//3)*3
  for i in range(3):
    for j in range(3):
      if board[block_r+i][block_c+j] == number:
        return False
  return True
def solution():
  global board
  for row in range(0,9):
      for column in range(0,9):
          if board[row][column]==0:
              for number in range(1,10):
                  if possible(row,column,number):
                      board[row][column]=number
                      solution()
                      board[row][column]=0
              return
  print(np.matrix(board))
solution()
