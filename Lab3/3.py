# def is_plusone_dictionary(d):
#     return_value = False
#     prev_val = -1
#     cnt = 0
#     for key in d:
#         if (cnt == 0):
#             prev_val = key
#         else:
#             if(key - prev_val != 1):
#                 return return_value
#             else:
#                 prev_val = key
#         cnt += 1
#         if(d[key] - prev_val != 1):
#             return return_value
#         else:
#             prev_val = d[key]
#     return_value = True
#     return return_value

def is_plusone_dictionary(d):
    dict_list = []
    for key in d:
        dict_list.append(key)
        dict_list.append(d[key])
    for index in range(1,len(dict_list)):
        if dict_list[index] - dict_list[index - 1] != 1:
            return False
    return True


dict = {1:2 , 3:4, 5:6}

#print(is_plusone_dictionary(dict))

for i in dict:
    print(i)
    print(dict[i])