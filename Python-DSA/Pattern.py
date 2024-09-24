
# Square pattern
def squarePattern():
    for i in range(0, 4):
        for j in range(0, 4):
            print("* ", end="")
        print("")

# pattern 2 
def pattern_2():
    for i in range(0, 6):
        for j in range(i):
            print("* ", end="")
        print("")

# pattern 3
def pattern_3():
    for i in range(1, 6):
        for j in range(1, i):
            print(j, " ", end="")
        print("")

# pattern 4 
def pattern_4():
    for i in range(5):
        for j in range(1 , 5 - i):
            print("* ", end="")
        print("")

# pattern 5 
def pattern_5():
    for i in range(5):
        for j in range(1 , 5 - i):
            print( j ," ", end="")
        print("")

# pattern 6
def pattern_6(n):
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        print('*' * (2 * i + 1), end='')
        print()

# pattern 7
def pattern_7(n):
    for i in range(n):
        print(' ' * i, end="")
        print('*' * (2 * (n - i) - 1), end='')
        print()

# pattern 8 
def pattern_8(n):
    for i in range(2*n):
        if i <= n:
            stars = i 
        else: 
            stars = 2 * n - i 
        
        print("*" * stars)

# pattern 9 
def pattern_9(n):
    for i in range(2*n):
        if i % 2 == 0:
            start = 1
        else: 
            start = 0
        
        for j in range(i):
            print(start, end='')
            start = 1 - start
        print()

# pattern 10
def pattern_10(n):
    space = 2*(n - 1)
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        
        print(' '*space, end="")

        for j in range(i, 0, -1):
            print(j, end="")
        
        print()
        space -= 2

# pattern 11
def pattern_11(n):
    num = 1
    for i in range(n + 1):
        for j in range(i):
            print(num, end='')
            num = num + 1
        print()

# pattern 12
def pattern_12(n):
    for i in range(n + 1):
        for ch in range(ord('A'), ord('A') + i + 1):
            print(chr(ch), end=' ')
        print()

# pattern 13
def pattern_13(n):
    for i in range(n + 1):
        for ch in range(ord('A'), ord('A') + (n - i - 1)):
            print(chr(ch), end=' ')
        print()

# pattern 14
def pattern_14(n):
    for i in range(n):
        ch = chr(ord('A') + i)
        for j in range(i + 1):
            print(ch, end=" ")
        print()

# pattern 15
def pattern_15(n):
    iniS = 0
    for i in range(n):
        for j in range(n - i):
            print('*', end='')
        for j in range(iniS):
            print(' ', end='')
        for j in range(n - i):
            print('*', end='')
        iniS += 2
        print()  
    
    iniS = 2 * (n - 1)  
    
    for i in range(n):
        for j in range(i + 1):
            print('*', end='')
        for j in range(iniS):
            print(' ', end='')
        for j in range(i + 1):
            print('*', end='')
        iniS -= 2
        print()

def pattern_16(n):
    for i in range(1, n + 1):
        print('*' * i, end='')
        print(' ' * (2 * (n - i)), end='')
        print('*' * i)
    
    for i in range(n - 1, 0, -1):
        print('*' * i, end='')
        print(' ' * (2 * (n - i)), end='')
        print('*' * i)

def pattern_17(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def pattern_18(n):
    size = 2 * n - 1
    for i in range(size):
        for j in range(size):
            top = i
            left = j
            right = (2 * n - 2) - j
            down = (2 * n - 2) - i
            value = n - min(top, left, right, down)
            print(value, end='')
        print()

n = 5
squarePattern()
pattern_2()
pattern_3()
pattern_4()
pattern_5()
pattern_6(n)
print("\n")
pattern_7(n)
print("\n")
pattern_8(n)
print("\n")
pattern_9(n)
print("\n")
pattern_10(n)
print("\n")
pattern_11(n)
print("\n")
pattern_12(n)
print("\n")
pattern_13(n)
print("\n")
pattern_14(n)
print("\n")
pattern_15(n)
print("\n")
pattern_16(n)
print("\n")
pattern_17(n)
print("\n")
pattern_18(n)