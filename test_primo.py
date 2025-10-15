n = 1

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2:
        return False

    for i in range(3, int(n ** 0.5), 2):
        if n % i == 0:
            return False 
    return True

status = "Primo" if is_prime(n) else "Não é Primo"


print(status)