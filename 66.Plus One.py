digits = [1,2,3,4]
num = len(digits)-1
for i in range(len(digits)):
    digits[i] = digits[i] * (10**num)
    num -= 1

print(digits)  
total = sum(digits)
print(total)