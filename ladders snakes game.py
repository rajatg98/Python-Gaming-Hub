
#SNAKES AND LADDERS GAME CODE BY RAJAT GUPTA
#initially we assume all the four players to be at position zero.
player1 = 0
player2 = 0
player3 = 0
player4 = 0

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


#code for snakes and ladders position
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
while player1 < 100 or player2 < 100 or player3 < 100 or player4 < 100:
	print "Its turn of player1\n"
	player1 = rolldice(player1)
	player1 = snakes_and_ladders_position(player1)
	print "Current position of Player1:",player1,"and Player2:",player2,"and Player3:",player3,"and Player4:",player4

	if player1 > 99:
		print "Winner of the game is player1"
		break

	print "Its turn of player2\n"
	player2 = rolldice(player2)
	player2 = snakes_and_ladders_position(player2)
	print "Current position of Player1:",player1,"and Player2:",player2,"and Player3:",player3,"and Player4:",player4

	if player2 > 99:
		print "Winner of the game is player2"
		break
	
	print "Its turn of player3\n"
	player3 = rolldice(player3)
	player3 = snakes_and_ladders_position(player3)
	print "Current position of Player1:",player1,"and Player2:",player2,"and Player3:",player3,"and Player4:",player4

	if player3 > 99:
		print "Winner of the game is player3"
		break
	
	print "Its turn of player4\n"
	player4 = rolldice(player1)
	player4 = snakes_and_ladders_position(player4)
	print "Current position of Player1:",player1,"and Player2:",player2,"and Player3:",player3,"and Player4:",player4

	if player4 > 99:
		print "Winner of the game is player4"
		break
