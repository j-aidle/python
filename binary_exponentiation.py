A = int(input())
B = int(input())

def power(A,B):
    if (B ==0):
        return 1
    res = power(A, B//2)
    if (B % 2):
        return res*res*A
    else:
        return res*res

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(power(A,B))


