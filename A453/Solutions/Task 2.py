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
c = str(input("What class are you in?"))
c = 'c' + c + '.txt' #This modifies the string 'c' to be in the format of
#'cn.txt' in which n is the class number. This removes the need to have 3 if
#statements to accomplish the same task.
for i in range(0, 10):
    Question()
print("{0}, you have scored {1} out of 10.".format(name,score))
with open(c, 'a') as f:#This uses the variable 'c' to open the correct file
#for the class
    f.write('%s %s\n' % (score, name))
    f.close
