i = 0
while(i <= 5):
    print("The value of i is" , i)
    i += 1  # i = i+1
print("Finished the program")
#print the sum of value
num = 1
sum = 0
print("Enter any number. Please Enterd the 0 for exit the program")
while num != 0:
    num = float(input("Number ?"))
    sum = sum + num;
    print(sum)
# guse number
import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')
# resvers a string
word = input("Enter any world")
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


