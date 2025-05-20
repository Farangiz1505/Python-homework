 1. is_prime(n) funksiyasi
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Misollar
print(is_prime(4))  # False
print(is_prime(7))  # True


2. digit_sum(k) funksiyasi

def digit_sum(k):
    return sum(map(int, str(k)))

# Misollar
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7

3. 2 ning darajalarini chiqaruvchi funksiya

def powers_of_two(N):
    k = 1
    result = []
    while 2**k <= N:
        result.append(2**k)
        k += 1
    print(*result)

# Misol
powers_of_two(10)  # 2 4 8
