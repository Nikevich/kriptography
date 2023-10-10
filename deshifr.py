def Gamma(y):
    gamma_array = [y]

    for i in range(41):
        y = (7 * y + 11) % 32
        gamma_array.append(y)
    
    return gamma_array
    

# array = [3, 6, 17, 6, 3, 11, 1, 3, 18, 6, 4, 5, 1, 17, 3]

# print(len(array))

y = 22
gamma = Gamma(y)

cArr = [1, 24, 29, 28, 8, 28, 4, 1, 8, 5, 28, 14, 24, 9, 14, 3, 30, 21, 1, 18, 26, 27, 17, 6, 4, 6, 4, 28, 18, 4, 3, 11, 10, 4, 17, 28, 11, 9, 17, 21, 1]

# for i in range(len(array)):
#     cArr.append((array[i] - 1 + gamma[i]) % 32 + 1)

# print(cArr)

bArr = []

for i in range(len(cArr)):
    bArr.append(((cArr[i] - 1 - gamma[i]) % 32 + 1))

print(bArr)

