def is_prime(n):
    if n < 2:
        return False
    if n < 4:            # 2 aur 3 prime hain
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:    # sirf sqrt(n) tak check karna kaafi hai
        if n % i == 0:
            return False
        i += 2           # even numbers skip
    return True


num = int(input("Number daalo: "))

if is_prime(num):
    print(f"{num} prime number hai")
else:
    print(f"{num} prime number nahi hai")
    
print("code End ho gaya")
