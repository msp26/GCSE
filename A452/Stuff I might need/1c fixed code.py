def mystery(n):
    a, b = 0, 1
    while a < n:
        print (a)
        a, b = b, a + b

while True:
    print("Please enter a number: ")
    n = int(input())
    mystery(n)
