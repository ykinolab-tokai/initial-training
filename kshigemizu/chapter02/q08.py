for i in range(2,101):
    is_prime = True
    for j in range(2, i-1):
        if i % j == 0:
            break
    if is_prime:
        print(i)