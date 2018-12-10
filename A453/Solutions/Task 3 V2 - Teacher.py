c = int(input('What class do you want to analyse? (1, 2, or 3)'))
f = open('data.txt', 'r').read()
a = eval(f)
classdata = a.get(c)
mode = str(input('How would you like to sort and view the data? (a = alphabetically with highest score, b = high > low with highest score, c = high > low with average score)\n'))
if mode == 'a':
    classdata.sort(key=lambda x: x[0])
    #This sorts the data alphabetically it looks at the first item
    for n in classdata:
        if len(n) == 2:
            maxi = n
        if len(n) == 3:
            maxi = max(n[1],n[2])
        if len(n) == 4:
            maxi = max(n[1],n[2],n[3])
        print('{0}\t{1}'.format(n[0],maxi))
    #This outputs the name and highest score for each student
elif mode == 'b':
    classdata.sort(key=lambda x: max(x[1],x[2],x[3]), reverse=True)
    #This sorts the data from low to high. The reverse argument then reverses this making the order high to low instead.
    for n in classdata:
        if len(n) == 2:
            maxi = n
        if len(n) == 3:
            maxi = max(n[1],n[2])
        if len(n) == 4:
            maxi = max(n[1],n[2],n[3])
        print('{0}\t{1}'.format(n[0],maxi))
    #This outputs the name and highest score for each student
elif mode == 'c':
    for n in classdata:
        if len(n) == 2:
            average = n
        if len(n) == 3:
            average = (n[1]+n[2])/2
        if len(n) == 4:
            average = (n[1]+n[2]+n[3])/3
        print('{0}\t{1}'.format(n[0],maxi))
        #This averages the data. It adds all the scores together then divides it by three.
        for i in range(3):
            n.pop()
        #This removes all 3 original scores from the student's sub-list
        n.append(average)
        #This appends the average score onto the sub-list
    classdata.sort(key=lambda x: x[1], reverse=True)
    
    for n in classdata:
        print('{0}\t{1}'.format(n[0],n[1]))
