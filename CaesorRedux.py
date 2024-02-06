n = int(input())

def caesar_cipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char == ' ':
            result += ' '
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

for _ in range(n):
    shift = int(input())
    message = input().strip()
    if "the " in message:
       
        shift *= -1
        result = caesar_cipher(message, shift)
        print(result)
    else:
        
        result = caesar_cipher(message, shift)
        print(result)
