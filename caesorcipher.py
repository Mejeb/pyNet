def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char == ' ':
            result += ' '
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
    return result

n = int(input())

for _ in range(n):
    shift = int(input())
    message = input().strip()
    if "the " in message:
        result = caesar_cipher(message, shift)
    else:
   
        result = caesar_cipher(message, -shift)
    print(result)
