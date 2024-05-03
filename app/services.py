import random
import math


# Tim uoc chung lon nhat
def get_gcd(n, m):
    max_number = n if n > m else m
    min_number = n if m > n else m
    while min_number != 0:
        temp = min_number
        min_number = max_number % min_number
        max_number = temp
    return max_number
    

# Tim so nguyen to cung nhau cua n
def get_coprime(n):
    gcd = 0
    while gcd != 1:
        i = random.randint(1, n)
        gcd = get_gcd(i, n)
    return i
        

def calculator_d(n, e):
    for i in range(3, n):
        if (e * i) % n == 1:
            return i


# Phuong phap ma hoa bao mat
def calculator_public_key(i, e, n):
    end = 2 ** (i-1)
    m = random.randint(1,end)
    c = (m ** e) % n
    return c, m

def calculator_private_key(c, d, n):
    m = (c ** d) % n
    return m

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def get_prime(middle):
    middle = int(middle / 2)
    p = random.randint(2,middle)
    while not is_prime(p):
        p = random.randint(2,middle)
    return p
    
def get_p_q(key_length):
    start = 2 ** (key_length - 1)
    end = 2 ** key_length
    middle = end - start
    while True:
        p = get_prime(middle)
        q = get_prime(middle)
        if p * q  > start and p * q < end:
            break
    
    return p, q
        


def generate_key(key_length):
    p, q = get_p_q(key_length)
    print('P: ', p)
    print('Q: ', q)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    print('N: ', n)
    print('Phi N: ', phi_n)
    e = get_coprime(phi_n)
    print('E: ', e)
    d = calculator_d(phi_n, e)
    print('D: ', d)
    return n, e, d

def encrypt(message, e, n):
    encode = [ord(m) for m in message]

    message_encrypt = []
    char_length = []
    for c in encode:
        char_encrypt = (c ** e) % n
        message_encrypt.append(char_encrypt)
        char_length.append(len(str(char_encrypt)))
        
    message_encrypt = ''.join(str(c) for c in message_encrypt)
    char_length = ''.join(str(c) for c in char_length)
    return message_encrypt + '010' + char_length
    
    
def decrypt(message_encrypt, d , n):
    message_decrypt = [] 
    data_encrypt = message_encrypt.split('010')
    message_encrypt = data_encrypt[0]
    char_length = data_encrypt[1]
    index = 0
    for length in char_length:
        m = ''
        for i in range(0, int(length)):
            m += message_encrypt[index+i]
        m = int(m)
        char_decrypt = (m ** d) % n
        message_decrypt.append(char_decrypt)
        index = index + int(length)

    message = "".join(chr(m) for m in message_decrypt)
    return message
    

# def main():
#     message = input('Message: ')
#     key_length = int(input('Enter your key length (bit): '))
#     phi_n, e, d = generate_key(key_length)
#     message_encrypt = encrypt(message, e, phi_n)
#     print(message_encrypt)
#     print(''.join(str(c) for c in message_encrypt))
#     message_decrypt = decrypt(message_encrypt, d, phi_n)
#     print(message_decrypt)
    
# main()