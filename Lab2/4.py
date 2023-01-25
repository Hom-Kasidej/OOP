nums = input().split()

def count_minus(_list):
    ans = [num for num in _list if int(num) < 0]
    return len(ans)

print(count_minus(nums))