import numpy as np

data = [line.rstrip("\n") for line in open("04.txt", "r").readlines()]
balls = [int(ball) for ball in data[0].split(",")] # split bals by , and make them ints
boards = [row.split() for row in data[1:]] # get the boards
rows = [row for row in boards if row] # remove empty strings
boards = np.array([rows[index:index+5] for index, row in enumerate(rows) if index % 5 == 0]).astype(np.float) # split rows into boards


def check_if_bingo(boards):
    
    for n, board in enumerate(boards):
                
        for row in board:
            if np.all(np.isnan(row)):
                return n, board
            
    
        for col in board.T:
            if np.all(np.isnan(col)):
                return n, board
    return n, board

winners = []
scores = []
winning_boards = []

for ball in balls:
    marks = np.where(boards==ball)
    boards[marks] = np.nan
    n, bingo_board = check_if_bingo(boards)
    
    print(bingo_board)
    if n not in winners:
        winners.append(n)
        scores.append(np.nansum(bingo_board) * ball)
        winning_boards.append(np.copy(bingo_board))


#     if bingo_boards:
#         break

# for bingo_board in bingo_boards:
#     #print(bingo_board)
#     print(np.nansum(bingo_board) * ball)
print(scores)
print(winning_boards)
