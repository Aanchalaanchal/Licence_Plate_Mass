def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if s[0:2].isalpha() == False:
        return False
    i = [x.isdigit() for x in s].index(True)
    if s[i] == '0':
        return False
    if s[i:len(s)].isdigit() == False:
        return False
    for char in s:
        if char in ['.', ' ', '?', ',', '!', ]:
            return False
    return True

main()
