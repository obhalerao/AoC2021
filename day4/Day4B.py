def wins(board):
    for i in range(5):
        if(sum(board[i]) == -5):
            return True
    for j in range(5):
        if(sum([board[i][j] for i in range(5)]) == -5):
            return True
    return False

def sun(board):
    s = 0
    for i in range(5):
        for j in range(5):
            s+=max(0, board[i][j])
    return s

lines = [l.strip() for l in open("../input.txt").readlines()]

order = [int(i) for i in lines[0].split(',')]

boards = []

curr_board = [[0 for i in range(5)] for j in range(5)]
for line in range(2, len(lines)):
    linen = line-2
    if linen % 6 == 5:
        boards.append(curr_board)
        curr_board = [[0 for i in range(5)] for j in range(5)]
    else:
        curr_arr = [int(i) for i in lines[line].split()]
        curr_board[linen%6] = curr_arr
boards.append(curr_board)

won = [False for i in range(len(boards))]

for num in order:
    for board in boards:
        for i in range(5):
            for j in range(5):
                if(board[i][j] == num):
                    board[i][j] = -1
    for idx, board in enumerate(boards):
        if(wins(board)):
            won[idx] = True
            if(sum(won) == len(won)):
                print(num*sun(board))
                exit()

