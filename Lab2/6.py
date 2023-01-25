list1 = input().split()
list2 = input().split()

def add2List(_list1,_list2):
    _returnList = [int(_list1[index]) + int(_list2[index]) for index in range(len(_list1))]
    return _returnList

print(add2List(list1,list2))