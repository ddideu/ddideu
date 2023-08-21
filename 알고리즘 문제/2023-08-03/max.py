arr = [list(map(int,input().split())) for _ in range(9)] 
max_row = 0
max_col = 0
max_arr = -1  
for row in range(9):
    for col in range(9):
        if max_arr <= arr[row][col]:
            max_row = row
            max_col = col
            max_arr = arr[row][col]
    
print(max_arr)
print(max_row + 1, max_col + 1)
