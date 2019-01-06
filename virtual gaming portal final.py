#VIRTUAL GAMING PORTAL CODING

#100m sprint code
def sprint():
        import msvcrt
        import time
        f2=open('score1.txt','r')
        high_score=f2.read()
        f2.close()
        f3=open('name.txt','r')
        name=f3.read()
        f3.close()
        while True:
                distance = int(0)
                print("\n--------------------------------------------------------------")
                print('\n\nWelcome to the 100m sprint, tap z and x rapidly to move!')
                print('* = 10m')
                print("\n**Current record: " + high_score + "s, by: " + name)
                print('\nPress enter to start')
                raw_input()
                print('Ready...')
                time.sleep(1)
                print('GO!')

                start_time = time.time()
                while distance < 100:

                        k1 = msvcrt.getch().decode('ASCII')
                        if k1 == 'z':
                                k2 = msvcrt.getch().decode('ASCII')
                                if k2 == 'x':
                                        distance += 1
                                        if distance == 50:
                                                print("* You're halfway there!")
                                        elif distance % 10 == 0:
                                                print('*')

                fin_time = time.time() - start_time
                fin_time = round(fin_time,2)


                print('Well done you did it in...')
                print(fin_time)
                bs=float(high_score)
             
                if fin_time < bs:
                        print("Well done you've got a new high score ")
                        name = raw_input("Please enter your name : ")
                        f1=open('score1.txt','w')
                        f1.write(str(fin_time))
                        f1.close()
                        f4=open('name.txt','w')
                        f4.write(name)
                        f4.close()
                        print 'high score successfully updated'

                welcome()

##################################################################################################

#minesweeper code
def minesweeper():
    import random
    import re
    import time
    from string import ascii_lowercase


    def setupgrid(gridsize, start, numberofmines):
        emptygrid = [['0' for i in range(gridsize)] for i in range(gridsize)]

        mines = getmines(emptygrid, start, numberofmines)

        for i, j in mines:
            emptygrid[i][j] = 'X'

        grid = getnumbers(emptygrid)

        return (grid, mines)


    def showgrid(grid):
        gridsize = len(grid)

        horizontal = '   ' + (4 * gridsize * '-') + '-'

        # Print top column letters
        toplabel = '     '

        for i in ascii_lowercase[:gridsize]:
            toplabel = toplabel + i + '   '

        print(toplabel + '\n' + horizontal)

        # Print left row numbers
        for idx, i in enumerate(grid):
            row = '{0:2} |'.format(idx + 1)

            for j in i:
                row = row + ' ' + j + ' |'

            print(row + '\n' + horizontal)

        print('')


    def getrandomcell(grid):
        gridsize = len(grid)

        a = random.randint(0, gridsize - 1)
        b = random.randint(0, gridsize - 1)

        return (a, b)


    def getneighbors(grid, rowno, colno):
        gridsize = len(grid)
        neighbors = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                elif -1 < (rowno + i) < gridsize and -1 < (colno + j) < gridsize:
                    neighbors.append((rowno + i, colno + j))

        return neighbors


    def getmines(grid, start, numberofmines):
        mines = []
        neighbors = getneighbors(grid, *start)

        for i in range(numberofmines):
            cell = getrandomcell(grid)
            while cell == start or cell in mines or cell in neighbors:
                cell = getrandomcell(grid)
            mines.append(cell)

        return mines


    def getnumbers(grid):
        for rowno, row in enumerate(grid):
            for colno, cell in enumerate(row):
                if cell != 'X':
                    # Gets the values of the neighbors
                    values = [grid[r][c] for r, c in getneighbors(grid,
                                                                  rowno, colno)]

                    # Counts how many are mines
                    grid[rowno][colno] = str(values.count('X'))

        return grid


    def showcells(grid, currgrid, rowno, colno):
        # Exit function if the cell was already shown
        if currgrid[rowno][colno] != ' ':
            return

        # Show current cell
        currgrid[rowno][colno] = grid[rowno][colno]

        # Get the neighbors if the cell is empty
        if grid[rowno][colno] == '0':
            for r, c in getneighbors(grid, rowno, colno):
                # Repeat function for each neighbor that doesn't have a flag
                if currgrid[r][c] != 'F':
                    showcells(grid, currgrid, r, c)


    def playagain():
        choice = raw_input('Play again? (y/n): ')

        return choice.lower() == 'y'


    def parseinput(inputstring, gridsize, helpmessage):
        cell = ()
        flag = False
        message = "Invalid cell. " + helpmessage

        pattern = r'([a-{}])([0-9]+)(f?)'.format(ascii_lowercase[gridsize - 1])
        validinput = re.match(pattern, inputstring)

        if inputstring == 'help':
            message = helpmessage

        elif validinput:
            rowno = int(validinput.group(2)) - 1
            colno = ascii_lowercase.index(validinput.group(1))
            flag = bool(validinput.group(3))

            if -1 < rowno < gridsize:
                cell = (rowno, colno)
                message = ''

        return {'cell': cell, 'flag': flag, 'message': message}


    def playgame():
        gridsize = 9
        numberofmines = 10

        currgrid = [[' ' for i in range(gridsize)] for i in range(gridsize)]

        grid = []
        flags = []
        starttime = 0

        helpmessage = ("Type the column followed by the row (eg. a5). "
                       "To put or remove a flag, add 'f' to the cell (eg. a5f).")

        showgrid(currgrid)
        print(helpmessage + " Type 'help' to show this message again.\n")

        while True:
            minesleft = numberofmines - len(flags)
            prompt = raw_input('Enter the cell ({} mines left): '.format(minesleft))
            result = parseinput(prompt, gridsize, helpmessage + '\n')

            message = result['message']
            cell = result['cell']

            if cell:
                print('\n\n')
                rowno, colno = cell
                currcell = currgrid[rowno][colno]
                flag = result['flag']

                if not grid:
                    grid, mines = setupgrid(gridsize, cell, numberofmines)
                if not starttime:
                    starttime = time.time()

                if flag:
                    # Add a flag if the cell is empty
                    if currcell == ' ':
                        currgrid[rowno][colno] = 'F'
                        flags.append(cell)
                    # Remove the flag if there is one
                    elif currcell == 'F':
                        currgrid[rowno][colno] = ' '
                        flags.remove(cell)
                    else:
                        message = 'Cannot put a flag there'

                # If there is a flag there, show a message
                elif cell in flags:
                    message = 'There is a flag there'

                elif grid[rowno][colno] == 'X':
                    print('Game Over\n')
                    showgrid(grid)
                    if playagain():
                        playgame()
                    return

                elif currcell == ' ':
                    showcells(grid, currgrid, rowno, colno)

                else:
                    message = "That cell is already shown"

                if set(flags) == set(mines):
                    minutes, seconds = divmod(int(time.time() - starttime), 60)
                    print(
                        'You Win. '
                        'It took you {} minutes and {} seconds.\n'.format(minutes,
                                                                          seconds))
                    showgrid(grid)
                    if playagain():
                        playgame()
                    return

            showgrid(currgrid)
            print(message)


    playgame()
    welcome()


###############################################################################################

#catch the thief code
from Tkinter import *
from random import *

def catchthethief():

    def do_event(event):
        print("{},{}".format(event.x,event.y))

    def jump(event):
        app.hello_b.place(relx=random(),rely=random())

    class App:
        def __init__(self,master):
            frame = Frame(master)
            master.geometry("160x160")
            master.title("Catch the Thief")
            master.bind("<Button-1>",do_event)
            master.bind("<Button-1>",do_event)
            frame.pack()

            self.hello_b = Button(master,text="Thief",command=sys.exit)
            self.hello_b.bind("<Enter>",jump)
            self.hello_b.pack()


    root = Tk()

    app = App(root)

    root.mainloop()

    welcome()

###############################################################################################

def snakes__and_ladders():
        #initially we assume all the four players to be at position zero.
        player1 = 0
        player2 = 0

        #code for the checkboard.
        a = range(1,11)
        b = range(20,10,-1)
        c = range(21,31)
        d = range(40,30,-1)
        e = range(41,51)
        f = range(60,50,-1)
        g = range(61,71)
        h = range(80,70,-1)
        i = range(81,91)
        j = range(100,90,-1)
        print "Snakes and Ladders game"
        print j,'\n',i,'\n',h,'\n',g,'\n',f,'\n',e,'\n',d,'\n',c,'\n',b,'\n',a


        #code for snwelcome()akes and ladders position
        def snakes_and_ladders_position(n):
                #tells you about the position of snakes and ladders
                ladders = {3:24, 8:35, 36:79, 47:88, 60:81}
                snakes = {98:9, 93:75, 72:50, 62:40, 58:18, 46:5, 49:30,} 
                if ladders.has_key(n):
                        print "Its a ladder,Climb up"
                        n = ladders[n]
                elif snakes.has_key(n):
                        print "Its a snake!!,Come down"
                        n = snakes[n]
                return n


        #code for roll dice
        def rolldice(r):
                #generates the number of the dice
                import random
                d = random.randint(1,6)
                print 'The number generated is:', d
                d = r + d
                return d


        #code for the main game
        while player1 < 100 or player2 < 100:
                print "Its turn of player1\n"
                int1=raw_input()
                player1 = rolldice(player1)
                player1 = snakes_and_ladders_position(player1)
                print "Current position of Player1:",player1,"and Player2:",player2

                if player1 > 99:
                        print "Winner of the game is player1"
                        break

                print "Its turn of player2\n"
                int2=raw_input()
                player2 = rolldice(player2)
                player2 = snakes_and_ladders_position(player2)
                print "Current position of Player1:",player1,"and Player2:",player2

                if player2 > 99:
                        print "Winner of the game is player2"
                        break
        welcome()

##############################################################################################

def welcome():
        inp=raw_input('Press a to play 100m SPRINT, b to play MINESWEEPER, c to play CATCH THE THIEF, d to play SNAKES AND LADDERS')
        if inp=='a':
           print sprint()
        elif inp=='b':
            print minesweeper()
        elif inp=='c':
            print catchthethief()
        elif inp=='d':
            print snakes__and_ladders()

################################################################################################


print 'Welcome to the Virtual Gaming Portal'
print welcome()
