import random
ladders = {3:24, 7:10, 14:22, 21:37, 34:49, 39:46}
snakes = {5:1, 11:4, 18:10, 27:12, 41:32, 48:17}
pos1 = 0
pos2 = 0
def move(pos):
	moves = random.randint(1,6)
	print(f'You have rolled {moves}')
	pos = pos + moves
	if pos < 50:
		if pos in ladders:
			pos = ladders[pos]
			print(f'You have climbed using ladder to {pos}\n')
		elif pos in snakes:
			pos = snakes[pos]
			print(f'You have been bitten by a snake and moved to {pos}\n')
		else:
			print(f'Your pos is {pos}\n')
	return pos

while True:
	A = input("Player A Press enter to roll dice")
	pos1 = move(pos1)
	if pos1 >= 50:
		print("Player A wins")
		break

	B = input("Player B press enter to roll dice")
	pos2 = move(pos2)
	if pos2 >= 50:
		print("Player B wins")
		break



