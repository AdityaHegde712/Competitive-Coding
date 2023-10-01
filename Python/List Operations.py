if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        command = input().strip()
        if command[0:6] == "insert":
            position = int(command[7])
            num = int(command[9:])
            list.insert(position, num)
        elif command == "print":
            print(list)
        elif command[0:6] == "remove":
            list.pop(list.index(int(command[7:])))
        elif command[0:6] == "append":
            list.append(int(command[7:]))
        elif command == "sort":
            list.sort()
        elif command == "pop":
            list.pop()
        elif command == "reverse":
            list.reverse()
        else:
            pass
