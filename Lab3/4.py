def char_count(str):
    # return_dict = {}
    # for char in str:
    #     if(not char in return_dict):
    #         return_dict[char] = 1
    #     else:
    #         return_dict[char] += 1
    return_dict = {i:str.count(i) for i in str}
    return {i:str.count(i) for i in str}

print(char_count("language"))
