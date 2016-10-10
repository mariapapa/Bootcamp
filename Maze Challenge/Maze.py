#0: empty cell
#1: wall              #table 5*5 as in the given example
#2: ending cell
#3: visited cell



table = [[0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [0, 1, 1, 0, 0],
         [0, 1, 0, 0, 1],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 2, 0]]

def search(x, y):
    if table[x][y] == 2:
        print ("exit found at", (x, y))

    elif table[x][y] == 1:
        print ("wall at", (x, y))

    elif grid[x][y] == 3:
        print ("already visited at" (x, y))

    print ("visiting at" (x, y))

    grid[x][y] = 3       # mark as visited

search (1,1)
