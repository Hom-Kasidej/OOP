str = input()

up = 0
low = 0

list = []

for char in str:
    if(not((char >= "A" and char <= "Z") or (char >= "a" and char <= "z"))):
        continue
    elif(char.isupper() == True):
        up += 1
    else:
        low += 1
print(f"{low}\n{up}")