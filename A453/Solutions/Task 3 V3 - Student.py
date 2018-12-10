while True:
    from random import randint, choice
    score = 0
    inlist = False
    operators = ['+', '-', '*']
    def Question():
        global score
        while True:
            a, b = randint(1, 12), randint(1, 12)
            op = choice(operators)
            if a > b or op != '-':
                break
        ans = eval(str(a) + op + str(b))
        while True:
            try:
                attempt = int(input("What is {0} {1} {2}?".format(a,op,b)))
            except ValueError:
                print("This is not a number! Try again.")
                continue
            else:
                break
        if attempt == ans:
            print("Correct!")
            score += 1
        else:
            print("Wrong, the correct answer is {0}!".format(ans))
        return
    name = str(input("What is your name?"))
    while True:
        try:
            c = int(input("What class are you in? (1, 2, or 3)"))
        except ValueError:
            print("This is not a number! Try again.")
            continue
        else:
            if c == 1 or c == 2 or c == 3:
                break
    for i in range(0, 10):
        Question()
    print("{0}, you have scored {1} out of 10.".format(name,score))
    
    f = open('data.txt', 'r').read()
    a = eval(f)
    clist = a.get(c)
    for i in clist:
        if name in i:
            inlist = True
            i.append(score)
            if len(i) > 4:
                i.pop(1)
    if inlist == False:
        clist.append([name, score])
    a[c] = clist
    f = open('data.txt', 'w').write(str(a))
    exitprogram = bool(input("Do you want to exit this program [Enter 'True' to exit]"))
    if exitprogram == True:
        raise SystemExit
