import sys
import random

def GuessTheNumber(num):
    for i in range(1,4):
        print('Guess the Number? \n')
        gussNum = int(sys.stdin.buffer.readline().decode())
        if num == gussNum:
            return print('Correct')
        else:            
            print( str(i) + ' Incorret Guess. YOu have '+ str(3-i) + ' chances to guess.')
            if i == 3: print('Sorry,Game Over')


sys.stdout.buffer.write(b'Please enter the minimum value\n')
sys.stdout.flush()
minNum = int(sys.stdin.buffer.readline().decode())

sys.stdout.buffer.write(b'Please enter the maximum value\n')
sys.stdout.flush()
maxNum = int(sys.stdin.buffer.readline().decode())

if minNum >= maxNum:
    print('The minimum value exceeds the maximum value. Please try again')
    sys.exit()

num = random.randint(minNum, maxNum)
# print(num)

GuessTheNumber(num)
