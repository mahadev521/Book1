'''backtracking algorithm'''

def pathFinder(mat, position, N):
    # returns a list of the paths taken
    if position == (N - 1, N - 1):
        return [(N - 1, N - 1)]
    x, y = position
    #check if the position left to current is in favour
    if x + 1 < N and mat[x+1][y] == 1:
        a = pathFinder(mat, (x + 1, y), N)
        if a != None:
            return [(x, y)] + a
    #check if the position down to current is in favour
    if y + 1 < N and mat[x][y+1] == 1:
        b = pathFinder(mat, (x, y + 1), N)
        if b != None:
            return [(x, y)] + b


mat = [
    [1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1]
]

# mat = [[1, 1, 1, 1, 0], 
#        [0, 1, 0, 1, 0], 
#        [0, 1, 0, 1, 0], 
#        [0, 1, 0, 0, 0], 
#        [1, 1, 1, 1, 1]]


print(pathFinder(mat, (0, 0), 5))
