import random

print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")

count = 0
while count < 3:
    num = random.randint(1, 6)
    print(num)
    if num == 5:
        print("Sorry, you lose!")
        break
    count += 1
# else block will execute anytime the loop condition is evaluated to False
else:
    print("You win!")