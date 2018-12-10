from random import randint, choice
score = 0
operators = ['+', '-', '*']
def Question():
    global score
    a, b = randint(1, 12), randint(1, 12)
    op = choice(operators)
    ans = eval(str(a) + op + str(b))
    attempt = int(input("What is {0} {1} {2}?".format(a,op,b)))                                 
    if attempt == ans:
        print("Correct!")
        score += 1
    else:
        print("Wrong, the correct answer is {0}!".format(ans))
name = str(input("What is your name?"))
for i in range(0, 10):
    Question()
print("{0}, you have scored {1} out of 10.".format(name,score))
