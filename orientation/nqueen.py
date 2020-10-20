# the n*n board
n = 8
# Returns the check coordinates for a position (x,y) of the Queen
def check_pos(x,y):
    def diagonal_handler(l):
        return list(filter(lambda tup: not ((tup[0] <= 0) or (tup[0] > n)) and not ((tup[1] <= 0) or (tup[1] > n)),l))
    return set([(x,j) for j in range(1,n+1)]+[(i,y) for i in range(1,n+1)]+diagonal_handler([(x+i,y+i) for i in range(-2*n,2*n)])\
           +diagonal_handler([(x+i,y-i) for i in range(-2*n,2*n)])\
           +diagonal_handler([(x-i,y+i) for i in range(-2*n,2*n)])+diagonal_handler([(x-i,y-i) for i in range(-2*n,2*n)]))
#preloading all check positions for optimization
total_set={(x,y):check_pos(x,y)for x in range(1,n+1)for y in range(1,n+1)}
#returns check position for a list of queen position

def print_board(moves, n):  #prints board in a readable format 
    board = [["Q" if (i,j) in moves else "." for i in range(1,n+1)] for j in range(1,n+1)]
    for i in range(n):
        print()
        for j in range(n):
            print(board[i][j], end = " ")
    print("\n\n")

def connector(list_):
    check_places=set()
    [check_places.update(list(total_set[x])) for x in list_]
    return check_places

def solver(q_list,iter_):
    #for the last iteration ie till [(1,.).......(n-1,..)] is decided
    if iter_ == n :#checks if the n-1 positions are correct
        check_places=connector(q_list)
        q_rem = (n,{x for x in range(1, n + 1)}.difference({x[1] for x in q_list}).pop())
        if not(q_rem in check_places):
            q_list.append(q_rem)
            print_board(q_list,n)#if so prints the last remaining valid move
    else:
        for i in range(1,n+1):#recursion of a new loop inside loops for solving
            check_position=connector(q_list)
            if (iter_,i) in check_position :#check if the new position clashes the old queens check position
                q_list_lier=[x for x in q_list if x[0]==iter_]#later when the first solution on any row is found,it skips
                if q_list_lier:                               #because the q_list contains last old queen position
                    q_list.remove(q_list_lier.pop())          #where it was solved , so remove it if it exists
                continue
            q_list.append((iter_,i))
            solver(q_list,iter_+1)#recusion line
            q_list.pop()# remove the recent test queen data at the end of loop of that queen row
[solver(q_list=[(1,y)],iter_=2) for y in range(1,n+1) ]#run the first iteration from outside for simplicity