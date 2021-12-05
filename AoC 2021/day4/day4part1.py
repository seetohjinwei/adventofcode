def helper(board):
    def helper2(row):
        return list(map(int, row.split()))
    return list(map(helper2, board.split("\n")))

data = open("day4/a.in").read()
nums, data = data.split("\n\n", 1)
nums = list(map(int, nums.split(",")))
boards = list(map(helper, data.split("\n\n")))

def check_bingo(board):
    for row in range(5):
        row_count = 0
        for col in range(5):
            if board[row][col] == -1:
                row_count += 1
        if row_count == 5:
            return True
    for col in range(5):
        col_count = 0
        for row in range(5):
            if board[row][col] == -1:
                col_count += 1
        if col_count == 5:
            return True
    return False
    
def update(board, value):
    for row in range(5):
        for col in range(5):
            if board[row][col] == value:
                board[row][col] = -1
                return check_bingo(board)
    return False

def sum(board):
    result = 0
    for row in range(5):
        for col in range(5):
            if board[row][col] != -1:
                result += board[row][col]
    return result

for num in nums:
    for board in boards:
        if update(board, num):
            print(num * sum(board))
            exit()
