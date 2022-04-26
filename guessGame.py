import random
import math

def guessNumFun(chances=10):
	lower = 1
	upper = 100

	x = random.randint(lower, upper)
	print("\n\tYou've only ", chances, " chances to guess the integer!\n")

	count = 0
	vst=[]

	while count < chances:

		guess = int(input("Guess a number:- "))

		if guess<0 or guess>100:
			continue
		if guess in vst:
			print("You enter this before")
			continue
		vst.append(guess) 

		if x == guess:
			print("Congratulations you did it in ",count+1 , " try")
			return chances-count-1
		elif x > guess:
			print("U guessed too small!")
		elif x < guess:
			print("U Guessed too high!")

		count += 1

	if count >= chances:
		print("\nThe number is %d" % x)
		print("\tBetter Luck Next time!")
		return -1

f = open('data.txt', 'rt')
l=f.read()
total,win,lose= l.split(',')
print("you played ",total
	," game and win: ",win
	," lose :", lose)
flag = True
ret = 10
while flag:
	ret=guessNumFun(ret)
	total = int(total)+1
	if ret<=0:
		lose= int(lose) + 1
		ch=input("Do u want to play again(Y/N): ")
		if ch=='Y' or ch=='y':
			ret = 10
		else:
			flag=False
	else:
		win = int(win) + 1 
	f=open("data.txt",'w')
	f.write(str(total)+','+str(win)+','+str(lose))