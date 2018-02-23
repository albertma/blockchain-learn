from hashlib import sha256


x = 5
y = 0 #We don't know what y should be yet...

while sha256(f'{x * y}'.encode()).hexdigest()[-1] != "0":
    print(f'{y}'.encode())
    y += 1


print(f'The solution is y = {y}')
