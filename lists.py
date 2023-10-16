from random import randint

if __name__ == '__main__':
    N = int(input())

    lst = []

    while N > 0:
        operation = randint(0,7)
        if operation == 0:
            lst.append(randint(1,10))
        elif operation == 1:
            print(lst)
        elif operation == 2:
            lst.pop()
        elif operation == 3:
            lst.insert(randint(1,10,1),randint(0,len(lst) - 1,1))
        elif operation == 4:
            lst.reverse()
        elif operation == 5:
            lst.sort()
        elif operation == 6:
            if len(lst) > 2:
                lst.remove(lst[randint(0,len(lst) - 1),randint(0,len(lst) - 1)])
            else:
                continue
        N -= 1