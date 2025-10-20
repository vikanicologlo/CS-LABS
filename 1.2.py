def generate_permuted_alphabet(keyword: str) -> str:
    keyword = "".join(dict.fromkeys(keyword.upper()))
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    remaining = "".join([ch for ch in alphabet if ch not in keyword])
    return keyword + remaining


def caesar_permutation_cipher(text: str, key: int, keyword: str, mode: str) -> str:
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    permuted_alphabet = generate_permuted_alphabet(keyword)

    text = text.upper().replace(" ", "")
    result = ""

    for ch in text:
        if ch not in base_alphabet:
            raise ValueError("Text must contain only A–Z letters")
        idx = permuted_alphabet.index(ch)

        if mode == "c":
            new_idx = (idx + key) % len(permuted_alphabet)
        elif mode == "d":
            new_idx = (idx - key) % len(permuted_alphabet)
        else:
            raise ValueError("Mode must be 'c' (cipher) or 'd' (decipher')")
        result += permuted_alphabet[new_idx]
    return result


mode = input("c = cipher, d = decipher: ").strip().lower()
key = int(input("Key (0–25): "))
keyword = input("Keyword (min 7 symbols): ").strip()
message = input("A–Z: ")


if not (0 < key <= 25):
    raise ValueError("Key must be between 0 and 25")

if len(keyword) < 7:
    raise ValueError("Keyword must be at least 7 characters long")


output = caesar_permutation_cipher(message, key, keyword, mode)
print("Updated alphabet:", generate_permuted_alphabet(keyword))
print("Result:", output)