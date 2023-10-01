# Swap the case of every character in an accepted string
if __name__ == '__main__':
    print(''.join(list(i.upper() if i.islower() else i.lower() for i in list(input()))))