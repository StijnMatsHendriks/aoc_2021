import numpy as np

def prep_data():
    with open('04.txt') as f:
        calls, *boards = f.read().split('\n')

    calls = np.array(calls.split(','), int)
    boards = np.loadtxt(boards, int).reshape(-1,5,5)
    return boards, calls


def bingo(boards, calls):
    winners, scores = [], []
    boards_ = np.copy(boards)    
    for call in calls:
        for n, board in enumerate(boards_):
            if n not in winners and call in board:
                r, c = np.where(board==call)
                board[r,c] = -1
                if (board[r,:] < 0).all() or (board[:,c] < 0).all():
                    scores.append(board[board>0].sum() * call)
                    winners.append(n)
    return list(zip(winners, scores))

results = bingo(*prep_data())

print('bingo:', results[0])
print('bongo:', results[-1])