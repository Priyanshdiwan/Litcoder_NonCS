def substitution_cipher_encrypt(word, cipher):
    encrypted_word = ""
    for char in word:
        if char.isalpha():
            encrypted_word += cipher[char]
        else:
            encrypted_word += char
    return encrypted_word
def encrypt_word_with_key(word, key, operation):
    if not isinstance(key, int):
        print("Enter a valid key")
        return
    if operation not in ['addition', 'subtraction']:
        print("Invalid Operation")
        return
    if not word.isupper():
        print("Word should be in capitals")
        return
    cipher = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R',
              'J': 'Q', 'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I',
              'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}
    encrypted_word = substitution_cipher_encrypt(word, cipher)
    if operation == 'addition':
        encrypted_word = ''.join(chr((ord(char) - 65 + key) % 26 + 65) if char.isalpha() else char for char in encrypted_word)
    elif operation == 'subtraction':
        encrypted_word = ''.join(chr((ord(char) - 65 - key) % 26 + 65) if char.isalpha() else char for char in encrypted_word)
    print(encrypted_word)
key_input = int(input())
operation_input = input().strip()
word_input = input()
encrypt_word_with_key(word_input, key_input,operation_input)