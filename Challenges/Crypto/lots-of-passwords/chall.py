    def g_key(msg, key):
    # Convert the key to a list to allow for modification
    key = list(key)
    # If the message and key are the same length, return the key as is
    if len(msg) == len(key):
        return key
    else:
        # If the message is longer than the key, repeat the key to match the message length
        for i in range(len(msg) - len(key)):
            # Append the character at the current index modulo the key length to the key
            key.append(key[i % len(key)])
    # Join the list of characters back into a string and return
    return "".join(key)

def enc(msg, key):
    # Initialize an empty list to store the encrypted characters
    encrypted_text = []
    # Generate the key based on the message length
    key = g_key(msg, key)
    # Iterate over each character in the message
    for i in range(len(msg)):
        char = msg[i]
        # Check if the character is uppercase
        if char.isupper():
            # Encrypt uppercase characters
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        # Check if the character is lowercase
        elif char.islower():
            # Encrypt lowercase characters
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            # If the character is neither uppercase nor lowercase, leave it unchanged
            encrypted_char = char
        # Append the encrypted character to the list
        encrypted_text.append(encrypted_char)
    # Join the list of encrypted characters back into a string and return
    return "".join(encrypted_text)

def dec(msg, key):
    # Initialize an empty list to store the decrypted characters
    decrypted_text = []
    # Generate the key based on the message length
    key = g_key(msg, key)
    # Iterate over each character in the message
    for i in range(len(msg)):
        char = msg[i]
        # Check if the character is uppercase
        if char.isupper():
            # Decrypt uppercase characters
            decrypted_char = chr((ord(char) - ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        # Check if the character is lowercase
        elif char.islower():
            # Decrypt lowercase characters
            decrypted_char = chr((ord(char) - ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            # If the character is neither uppercase nor lowercase, leave it unchanged
            decrypted_char = char
        # Append the decrypted character to the list
        decrypted_text.append(decrypted_char)
    # Join the list of decrypted characters back into a string and return
    return "".join(decrypted_text)

encrypted_flag = "zhdwqmj{CPro5khGjcezVyag}"
with open('phished.txt', 'r') as f:
    for password in f:
        password = password.strip()
        decrypted_flag = dec(encrypted_flag, password)
        print(f"Trying password: {password}")
        print(f"Decrypted flag: {decrypted_flag}")
        if decrypted_flag.startswith("REDACTED"):
            print("Found the correct password!")
            break
