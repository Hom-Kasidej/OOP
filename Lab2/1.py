numbers = input().split()
numbers.sort()
#print(numbers)
index = 1
prev_num = numbers[0]
if prev_num == '0':
    while(numbers[index] == '0'):
        index += 1
    temp = numbers[0]
    numbers[0] = numbers[index]
    numbers[index] = temp

for num in numbers :
    print(num,end = " ")