def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        s = string[i:i+k]
        t = ""
        for j in s:
            if j not in t:
                t += j
        print(t)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)