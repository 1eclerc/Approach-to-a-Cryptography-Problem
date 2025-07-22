# Github: @1eclerc

# Libraries

import math
from itertools import permutations

# Applying Caesar cipher

def caesar_decrypt(text, shift):
    decrypted = ''
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            decrypted += chr((ord(c) - base - shift) % 26 + base)
        else:
            decrypted += c
    return decrypted

# Reversing

def reverse_text(text):
    return text[::-1]

# Applying Transposition algorithm

def transposition_decrypt(ciphertext, key):
    import math
    num_rows = math.ceil(len(ciphertext) / key)
    num_shaded_boxes = (num_rows * key) - len(ciphertext)
    
    plaintext = [''] * num_rows
    col = 0
    row = 0
    
    for symbol in ciphertext:
        plaintext[row] += symbol
        row += 1
        if (row == num_rows) or (row == num_rows - 1 and col >= key - num_shaded_boxes):
            row = 0
            col += 1
            
    return ''.join(plaintext)

# Brute Force

def brute_force_decrypt(cipher_text):
    steps = ['caesar', 'reverse', 'transposition'] # steps of the algorithm
    orderings = list(permutations(steps))
    possible_keywords = ['the', 'this', 'that', 'you', 'have', 'are', 'and', 'is', 'your', 'not']

    for order in orderings:
        for caesar_shift in range(1, 26):
            for trans_key in range(2, 11):
                text = cipher_text
                for step in order:
                    if step == 'caesar':
                        text = caesar_decrypt(text, caesar_shift) # if its Caesar, inform
                    elif step == 'reverse': # if its Reverse, inform 
                        text = reverse_text(text) 
                    elif step == 'transposition': # if its Transposition, inform
                        text = transposition_decrypt(text, trans_key)

                # Does it contain words that are similar in meaning to frequently used words?
                # If yes, mark it as a potential answer and keep
                lower_text = text.lower()
                if any(word in lower_text for word in possible_keywords):
                    print(f"[+] Muhtemel çözüm bulundu:")
                    print(f"    Sıra: {order}")
                    print(f"    Caesar shift: {caesar_shift}")
                    print(f"    Transposition sütun: {trans_key}")
                    print(f"    Mesaj: {text}")
                    print("-" * 80) # Line

# === Usage ===
cipher_text = "kavvkaappyt_vpasuuZynlvtjy__hl_luaJh!_dlP_knlLb__ll_c_,buu_whP" # The text that was provided by the problem
brute_force_decrypt(cipher_text) # Method