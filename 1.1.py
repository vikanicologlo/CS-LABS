
def caesar_cipher(text: str, key: int, mode: str) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = text.upper().replace(" ", "")
    result = ""

    for ch in text:
        if ch in alphabet:
            idx = alphabet.index(ch)
            if mode == "c":
                new_idx = (idx + key) % len(alphabet)
            elif mode == "d":
                new_idx = (idx - key) % len(alphabet)
            else:
                raise ValueError("Mode must be 'c' (cipher) or 'd' (decipher)")
            result += alphabet[new_idx]
        else:
            raise ValueError("Text must contain only A–Z letters")
    return result


mode = input("c = cipher, d = decipher: ").strip().lower()
key = int(input("Key (1–25): "))
message = input("(A–Z): ")

output = caesar_cipher(message, key, mode)
print("Result:", output)