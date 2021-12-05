with open("day4.in") as f:
    nums, data =  f.read().split("\n\n", 1)
nums = list(map(int, nums.split(",")))
boards = list(map(lambda board: list(map(lambda row: list(map(int, row.split())), board.split("\n"))), data.split("\n\n")))

def check_bingo(board):
    for row in range(5):
        if 5 == sum(1 for col in range(5) if board[row][col] == -1):
            return True
    for col in range(5):
        if 5 == sum(1 for row in range(5) if board[row][col] == -1):
            return True
    return False

def update(board, value):
    for row in range(5):
        for col in range(5):
            if board[row][col] == value:
                board[row][col] = -1
                return check_bingo(board)
    return False

def sum_board(board):
    return sum(val for row in board for val in row if val != -1)

s = set(range(len(boards)))
final = False
for num in nums:
    if not final:
        for i in s.copy():
            board = boards[i]
            if update(board, num):
                s.remove(i)
                if len(s) == 1:
                    final = True
                    index = s.pop()
    else:
        board = boards[index]
        if update(board, num):
            print(num * sum_board(board))
            exit()
