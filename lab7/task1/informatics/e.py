N = int(input())
array = list(map(int, input().split()))

#A
for i in range(0, N, 2):
    print(array[i])

#B
for num in array:
    if num % 2 == 0:
        print(num)

#C
count_positive = 0
for num in array:
    if num > 0:
        count_positive += 1

print(count_positive)

#D
count_greater = 0
for i in range(1, N):
    if array[i] > array[i - 1]:
        count_greater += 1

print(count_greater)

#E
for i in range(1, N):
    if array[i] * array[i - 1] > 0:
        print("YES")
        break
else:
    print("NO")

#F
count = 0
for i in range(1, N - 1):
    if array[i] > array[i - 1] and array[i] > array[i + 1]:
        count += 1

print(count)

#G
for i in range(N // 2):
    array[i], array[N - 1 - i] = array[N - 1 - i], array[i]

for num in array:
    print(num, end=' ')
