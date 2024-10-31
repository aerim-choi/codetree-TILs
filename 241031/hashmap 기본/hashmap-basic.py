n =int(input())

d = dict()
for _ in range(n):
    command = input().split()

    if command[0]=="add":
        d[int(command[1])] = int(command[2])
    elif command[0]=="find":
        if int(command[1]) in d:
            print(d[int(command[1])])
        else:
            print(None)
    else: #remove
        d.pop(int(command[1]))