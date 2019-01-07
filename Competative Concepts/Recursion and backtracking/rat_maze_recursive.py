def paths(maze, soln, i, j, m, n):
    if i == m - 1 and j == n - 1:
        # print the paths
        soln[i][j] = 1
        for i in range(0, m):
            for j in range(0, n):
                print(soln[i][j], end=" ")
            print("")
        print("")
        return True
    if i >= m or j >= n:
        return False
    if maze[i][j] == "x":
        return False
    # assuming the maze is solved through the current cell
    soln[i][j] = 1  # here soln is a local variable but pointing to val of the same soln in heap everytime
    check_right = paths(maze, soln, i, j + 1, m, n)
    check_down = paths(maze, soln, i + 1, j, m, n)
    # now all recursive calls made, time to backtrack
    soln[i][j] = 0
    if check_right or check_down:
        return True
    return False


if __name__ == "__main__":
    print("Please enter the no. of rows:")
    m = int(input())
    print("Pleaes enter the num of col")
    n = int(input())
    maze = [[None for x in range(n)] for y in range(m)]
    print("Pleaes enter the maze char row*col wise:")
    for i in range(0, m):
        for j in range(0, n):
            maze[i][j] = input()
    print("The maze:")
    for i in range(0, m):
        for j in range(0, n):
            print(maze[i][j], end=" ")
        print("")
    print("The different solutions are:")
    soln = [[0 for x in range(n)] for y in range(m)]
    if paths(maze, soln, 0, 0, m, n) == False:
        print("No solutions found!!")
