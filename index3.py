num = 76542
temp = 0
while num > 0:
    i = num % 10
    temp = (temp * 10) + i
    num = num // 10
print(temp)