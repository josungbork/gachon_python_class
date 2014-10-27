import random
import sys

def isMisTypedNumber(number):

	if isZeroNumber(number): endOfGame()
	if not (number.isdigit()): return True
	if not (isThreeFigures(number)): return True
	if isDuplicatedNumber(number): return True

	return False

def isZeroNumber(number):
	return True if number == "0" else False

def isThreeFigures(number):
	return True if len(number) == 3 else False

def isDuplicatedNumber(number):
	for digit in number:
		if number.count(digit) > 1:
			return True
	return False

def getStrikeOrBallDecision(game_number, users_number):
	strike_counter = 0
	ball_counter = 0
	result = []

	for digit in users_number:
		if game_number.count(digit) == 1:
			if users_number.index(digit) == game_number.index(digit):
				strike_counter += 1
			else:
				ball_counter += 1
	result.append(strike_counter)
	result.append(ball_counter)

	return result

def isThreeStrikes(number_of_strikes):
	return True if number_of_strikes == 3 else False

def getContinueGame():
	while 1:
		users_input = str(raw_input())

		if (isZeroNumber(users_input)): endOfGame()
		if (users_input.upper() == "YES"): return True		
		if (users_input.upper() == "NO"): endOfGame()
		
		print "You input wrong values"
		print "Do you want one more game (Yes/no)"

def endOfGame():
	print "Good bye. Have a nice day"
	sys.exit(1)

# Start Game
print "This is a three digit baseball game"

continue_game_flag = True
while continue_game_flag:

	print "If you input 0, this game will be finished"
	print "Input three figures to play baseball game: "

	game_number = str(random.randint(100,999))
	while (isDuplicatedNumber(game_number)):
		game_number = str(random.randint(100,999))
	print game_number
	
	game_counter = 0

	decision = [0,0]
	
	while not isThreeStrikes(decision[0]):
		users_number = str(raw_input())
		while (isMisTypedNumber(users_number)):
			print "Wrong Input!",
			print "Input three figures again: "
			users_number = str(raw_input())

		decision = getStrikeOrBallDecision(game_number, users_number)

		print "Stirke :",decision[0] , "Ball :", decision[1]
		game_counter += 1

	print "You win this game. You've played", game_counter , "times"
	print "Do you want one more game (Yes/no)"
	game_counter = 0
	continue_game_flag = getContinueGame()