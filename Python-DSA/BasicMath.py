
def count_digits(num):
    if num == 0:
        return 1
    num = abs(num)
    count = 0 
    while num > 0:
        last_digits = num % 10
        count = count + 1 
        num //= 10 
    return count 

def reverse_number(num):
    revNum = 0
    while num > 0:
        last_digits = num % 10
        revNum = (revNum * 10) + last_digits
        num //= 10
    return revNum

def palindrome(num):
    if num < 0:
        return False
    original_num = num
    rev_num = 0 
    while num > 0:
        last_digits = num % 10
        rev_num = (rev_num * 10) + last_digits
        num //= 10
    return original_num == rev_num

def armstrong_number(num):
    if num < 0:
        return False
    original_num = num 
    sum = 0 
    number_of_digits = len(str(num))
    while num > 0:
        last_digits = num % 10 
        sum += last_digits ** number_of_digits
        num //= 10
    
    return sum == original_num

def print_divisor(num):
    for i in range(1, num+1):
        if num % i == 0:
            print(i , end=' ')

def print_divisor_other(num):
    divisor = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisor.append(i)
            if i != num // i:
                divisor.append(num // i)
    divisor.sort()
    print(divisor)

def is_prime(num):
    if num <= 1:
        return False  

    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1

    if count == 2:
        print(f"prime num: {num} true")
    else:
        print(f"prime num: {num} false")


number = 7789
num2 = 141
num3 = 1634
print("count digits -> ", count_digits(number))
print("reverse number -> ", reverse_number(number))
print(f"palindrome : {num2} -> {palindrome(num2)}")
print(f"armstrong number: {num3} -> {armstrong_number(num3)}")
print("divisor of number: " , num2)
print_divisor(num2)
print_divisor_other(num2)
print()
is_prime(17)