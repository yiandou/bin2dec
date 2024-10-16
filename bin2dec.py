def bin2dec(num):

    decimal, i = 0, 0
    while num != 0:
        dec = num % 10
        decimal = decimal + dec * pow(2, i)
        num = num // 10
        i += 1
    return decimal

def dec2bin(num):
    binary = 0
    i = 1
    while num != 0:
        binary = binary + (num % 2) * i
        num = num // 2
        i = i * 10
    return binary

