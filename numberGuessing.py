#Users number guessing game using Python-3
#In this game user will be finding computers number
#importing random module for this program 
from random import randint

#To Do : computer
#Storing our secreat random number between 1 - 30;
secret_value  =  randint(1, 30)
print('I stored a good number in between 1 - 30 can you find it')

#lives;
live = 11

#To Do : human
for i in range (1, live):

	human_value = int(input('Enter the number which you guess its correct '))
	if human_value > secret_value:
		print('Sorry  your answer is too high ')
	elif human_value < secret_value:
		print('Sorry  your answer is too low ')
	else:
		break
#win / loss
if human_value == secret_value:
	print('yay you won you found it ')
else:
	print(f'you lost my answer was  {secret_value} ')
input('you program ended')