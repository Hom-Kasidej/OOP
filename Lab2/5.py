string = input()

def eng_only(_list):
    _returnString = [char for char in _list if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or char == ' ']
    return _returnString
for char in eng_only(string):
    print(char,end="")

