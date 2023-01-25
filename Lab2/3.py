x = [ [1, -3, 2], [-8, 5], [-1, -4, -3] ]

def minus_remove(_list):
    ans = [[num for num in sup_list if num >= 0] for sup_list in _list]
    return ans

print(minus_remove(x))