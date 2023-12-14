def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def dfs(row, col, index):
        if index == len(word):
            return True
        if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col]:
            return False
        if board[row][col] != word[index]:
            return False
        visited[row][col] = True
        result = (dfs(row + 1, col, index + 1) or
                 dfs(row - 1, col, index + 1) or
                 dfs(row, col + 1, index + 1) or
                 dfs(row, col - 1, index + 1))
        visited[row][col] = False
        return result
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == word[0]:
                visited = [[False] * cols for _ in range(rows)]
                if dfs(row, col, 0):
                    return "Yes"
    return "No" 
input_str = "4 4 good agcd eooh ijdl rfgt" 
input_arr = input_str.split(' ')
rows, cols, word = int(input_arr[0]), int(input_arr[1]), input_arr[2]
board = [list(input_arr[i+3]) for i in range(rows)]
string_array = input_arr[3:]

output = exist(board, word)
print(output)