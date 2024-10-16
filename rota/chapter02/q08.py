# 2から100までの素数を列挙するプログラム
prime = []
for p in range(2, 101):
    judge_prime = True
    for k in range(2, int(p ** 0.5) + 1):  
        if p % k == 0:
            judge_prime = False
            break
    if judge_prime:
        prime.append(p)

print(prime)  