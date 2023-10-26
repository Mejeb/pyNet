import base64

def decrypt_pass(password):
    decode_bytes = base64.b64decode(password)
    decode_data = decode_bytes.decode()
    print(f"decoded password is {decode_data}")
encode_strings = input("Enter the base64 string:\n")
decrypt_pass(encode_strings) 