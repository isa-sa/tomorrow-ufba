N = int(input())
2 <= N <= 10000

if N < 2:
    print("0")
       
else:
    primo = True
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            primo = False
            break

    if primo:
        print("1")
    else:
        print("0")