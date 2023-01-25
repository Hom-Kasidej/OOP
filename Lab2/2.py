words = input().split()
checked_char = input()

freq = [word.count(checked_char) for word in words]

print(freq)
    