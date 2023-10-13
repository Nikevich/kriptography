import operator
# Number 1

Arr = [1, 1, 0]
bArr = []
controllArr = []

for i in range(8):
    controllArr = Arr
    bArr.append(Arr[-1])
    print(bArr)
    Arr[0] = operator.xor(Arr[0], Arr[-1])

    for k in range(len(Arr) - 1):
        Arr[k+1] = controllArr[k]

print(Arr)