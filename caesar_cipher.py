upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def check_case(char):
    if "A"<= char <= "Z" :
        return "uppercase"
    elif "a" <= char <= "z" :
        return "lowercase"
    else :
        return "not a letter"

def encrypting(msg,key) :
    encrypted=""
    for i in range(len(msg)):
        char = msg[i]
        case = check_case(char)
        if case == "uppercase":
            index = upper_case.index(char)
            encrypted += upper_case[(index + key)%26]
        elif case == "lowercase" :
            index = lower_case.index(char)
            encrypted += lower_case[(index + key)%26]
        elif case == "not a letter":
            encrypted += char
    return encrypted

def decrypting(msg,key):
    decrypted=""
    for i in range(len(msg)):
        char = msg[i]
        case=check_case(char)
        if case == "uppercase":
            index = upper_case.index(char)
            decrypted += upper_case[(index - key)%26]
        elif case == "lowercase" :
            index = lower_case.index(char)
            decrypted += lower_case[(index - key)%26]
        elif case == "not a letter":
            decrypted += char
    return decrypted





message =input("enter the message to : ")
Key =int(input("enter the key: "))
encrypted_msg=encrypting(message,Key)
print("Encrypted message : ",encrypted_msg)
decrypted_msg=decrypting(encrypted_msg,Key)
print("decrypted message : ",decrypted_msg)

